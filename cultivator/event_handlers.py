from abc import ABC, abstractmethod
from cultivator.api_clients import PlatformAPIClient
from typing import Any

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

class IssueEventHandler(EventHandler):
    def __init__(self, client: PlatformAPIClient):
        self.client = client

    def handle_event(self, event_data: Any) -> None:
        # Implementation for handling issue events
        pass
