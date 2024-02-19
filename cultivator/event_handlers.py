from abc import ABC, abstractmethod
from cultivator.api_clients import PlatformAPIClient
from typing import Any
from enum import Enum, auto
from openai import OpenAI

from cultivator.models.issue import Issue, parse_issue


class EventHandler(ABC):
    @abstractmethod
    def handle_event(self, event_data: Any) -> None:
        pass


class PushEventHandler(EventHandler):
    def __init__(self, client: PlatformAPIClient):
        self.client = client

    def handle_event(self, event_data: Any) -> None:
        # Implementation for handling push events
        pass


class CodeEditType(Enum):
    ADDING_TESTS = auto()
    WRITING_NEW_CODE = auto()
    EDITING_EXISTING_CODE = auto()


class IssueEventHandler(EventHandler):
    def __init__(self, client: PlatformAPIClient, openaiClient: OpenAI):
        self.client = client
        self.openai = openaiClient

    def handle_event(self, event_data: Any) -> None:
        # Implementation for handling issue events

        issue = parse_issue(event_data)

        chat_completion = self.openai.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"Your task is to triage incoming change requests into distinct categories. Please always answer one of the following options: [{', '.join([member.name for member in CodeEditType])}] ",
                },
                {
                    "role": "user",
                    "content": f"What category does this request best match?\n\n{issue.title}\n{'=' * len(issue.title)}\n{issue.body}",
                },
            ],
            model="gpt-3.5-turbo",
        )

        print(chat_completion)
