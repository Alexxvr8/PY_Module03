#!/usr/bin/env python3
"""ft_data_alchemist: transform and filter player data with comprehensions."""


import random


def data_alchemist() -> None:
    """Build lists and dicts of player scores using comprehensions."""
    print("=== Game Data Alchemist ===")

    players = ["Luffy", "Zoro", "nami", "usopp", "Sanji",
               "chopper", "Robin", "franky", "brook"]
    capitalized = [p.capitalize() for p in players]
    already_cap = [p for p in players if p == p.capitalize()]
    scores = {name: random.randint(1, 1000) for name in capitalized}
    average = sum(scores.values()) / len(scores)
    high = {name: scores[name] for name in scores if scores[name] > average}

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {already_cap}")
    print()
    print(f"Score dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high}")


if __name__ == "__main__":
    data_alchemist()
    print("\n=== End of Program ===")
