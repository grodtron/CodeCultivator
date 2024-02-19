from cultivator.models.event import Event
from cultivator.event_handlers import EventHandler, PushEventHandler, IssueEventHandler
from cultivator.api_clients import GitHubAPIClient
from cultivator.models.platform_enum import Platform
from typing import Optional, Dict, Any
from openai import OpenAI


class EventHandlerFactory:
    @staticmethod
    def get_handler(
        event: Event, api_key: str, open_ai_api_key: str, config: Optional[Dict[str, Any]] = None
    ) -> EventHandler:
        platform_client_mapping = {Platform.GITHUB: GitHubAPIClient}

        if event.platform not in platform_client_mapping:
            raise NotImplementedError(
                f"Platform {event.platform.value} is not supported."
            )

        client_class = platform_client_mapping[event.platform]
        client = client_class(api_key, config)

        openai = OpenAI(api_key=open_ai_api_key)
        
        if event.platform == Platform.GITHUB:
            event_type = event.data.get("event_type")
            if "pull_request" in event.data:
                return PushEventHandler(client)
            elif "issue" in event.data:
                return IssueEventHandler(client, openai)
            else:
                raise ValueError(f"Event type {event_type} is not supported.")
        else:
            raise NotImplementedError(
                f"Handler for {event.platform.value} is not implemented."
            )
