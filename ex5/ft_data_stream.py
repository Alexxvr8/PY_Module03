#!/usr/bin/env python3
"""ft_data_stream.py: generate and consume game events using generators."""


import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    """Yield endless random (player, action) event tuples."""
    players = ["luffy", "zoro", "nami", "usopp", "sanji",
               "chopper", "robin", "franky", "brook"]
    actions = ["punch", "slash", "navigate", "cook", "sing",
               "shoot", "sail", "fight", "eat", "dream"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    """Yield and remove random events from the list until it is empty."""
    while len(events) > 0:
        i = random.randint(0, len(events) - 1)
        yield events.pop(i)


def data_stream() -> None:
    """Produce 1000 events, build a list of 10, then consume it randomly."""
    print("=== Game Data Stream Processor ===")
    gen = gen_event()

    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for _ in range(10):
        events.append(next(gen))
    print(f"\nBuilt list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    data_stream()
    print("\n=== End of Program ===")
