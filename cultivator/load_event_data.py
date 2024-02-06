from cultivator.models.platform_enum import Platform
from cultivator.models.event import Event
import os
import json


def load_event_data() -> Event:
    try:
        if "GITHUB_EVENT_PATH" in os.environ:
            platform = Platform.GITHUB
            event_path = os.environ["GITHUB_EVENT_PATH"]
            with open(event_path, 'r') as event_file:
                data = json.load(event_file)
            return Event(platform, data)
        else:
            raise ValueError("Platform cannot be detected.")
    except Exception as e:
        raise RuntimeError(f"Error loading event data: {e}")
