from abc import ABC, abstractmethod
from cultivator.api_clients import PlatformAPIClient

class EventHandler(ABC):
    @abstractmethod
    def handle_event(self, event_data):
        pass

class PushEventHandler(EventHandler):
    def __init__(self, client: PlatformAPIClient):
        self.client = client

    def handle_event(self, event_data):
        # Implementation for handling push events
        pass

class IssueEventHandler(EventHandler):
    def __init__(self, client: PlatformAPIClient):
        self.client = client

    def handle_event(self, event_data):
        # Implementation for handling issue events
        pass
