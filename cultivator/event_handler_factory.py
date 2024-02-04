from cultivator.models.event import Event
from cultivator.event_handlers import EventHandler, PushEventHandler, IssueEventHandler
from cultivator.api_clients import GitHubAPIClient
from cultivator.models.platform_enum import Platform
from typing import Optional

class EventHandlerFactory:
    @staticmethod
    def get_handler(event: Event, api_key: str, config: Optional[dict] = None) -> EventHandler:
        platform_client_mapping = {
            Platform.GITHUB: GitHubAPIClient
        }
        
        if event.platform not in platform_client_mapping:
            raise NotImplementedError(f"Platform {event.platform.value} is not supported.")
        
        client_class = platform_client_mapping[event.platform]
        client = client_class(api_key, config)

        if event.platform == Platform.GITHUB:
            event_type = event.data.get('event_type')
            if event_type == 'push':
                return PushEventHandler(client)
            elif event_type == 'issue':
                return IssueEventHandler(client)
            else:
                raise ValueError(f"Event type {event_type} is not supported.")
        else:
            raise NotImplementedError(f"Handler for {event.platform.value} is not implemented.")
