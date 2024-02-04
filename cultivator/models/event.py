from dataclasses import dataclass
from typing import Any
from cultivator.models.platform_enum import Platform

@dataclass
class Event:
    platform: Platform
    data: Any
