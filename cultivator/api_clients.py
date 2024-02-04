from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class PlatformAPIClient(ABC):
    @abstractmethod
    def perform_action(self) -> None:
        pass

class GitHubAPIClient(PlatformAPIClient):
    def __init__(self, api_key: str, config: Optional[Dict[str, Any]] = None):
        self.api_key = api_key
        self.config: Dict[str, Any] = config or {}

    def perform_action(self) -> None:
        # Implementation for GitHub API actions using self.api_key and self.config
        pass
