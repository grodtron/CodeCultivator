import argparse
from cultivator.models.event import Event
from cultivator.models.platform_enum import Platform
from cultivator.event_handler_factory import EventHandlerFactory
from cultivator.load_event_data import load_event_data
from typing import Optional


def main() -> None:
    parser = argparse.ArgumentParser(description="Process events.")
    parser.add_argument(
        "--api-key", type=str, required=True, help="API key for the platform"
    )

    parser.add_argument(
        "--open-ai-api-key", type=str, required=True, help="API key for OpenAI"
    )

    args = parser.parse_args()

    event = (
        load_event_data()
    )  # This would be replaced with the actual function to load event data

    print(repr(event))

    handler = EventHandlerFactory.get_handler(event, args.api_key, args.open_ai_api_key)
    handler.handle_event(event.data)


if __name__ == "__main__":
    main()
