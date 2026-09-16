#!/usr/bin/env python3
"""ft_achievement_tracker.py: generate and compare player achievement sets."""


import random


def gen_player_achievements() -> set[str]:
    """Return a random set of achievements picked from a fixed pool."""
    achievements = [
        "Haki", "Awakening", "Bounty", "Nakama", "Devilfruit",
        "Poneglyph", "Grandline", "Yonko", "Warlord", "Wano",
        "Sunny", "Ace", "Vivre", "Onepiece",
    ]
    n = random.randint(5, 9)
    return set(random.sample(achievements, n))


def achievement_tracker() -> None:
    """Generate achievement sets for players and analyze them with set ops."""
    print("=== Achievement Tracker System ===")

    players = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji",
               "Chopper", "Robin", "Franky", "Brook"]
    achievements = {}
    all_distinct: set[str] = set()

    for player in players:
        achievements[player] = gen_player_achievements()
        all_distinct = all_distinct.union(achievements[player])
        print(f"Player {player}: {achievements[player]}")
    print(f"\nAll distinct achievements: {all_distinct}")

    print()

    sets = list(achievements.values())
    common = sets[0]
    for s in sets[1:]:
        common = common.intersection(s)
    print(f"Common achievements: {common}")

    print()

    for player in players:
        others: set[str] = set()
        for other in players:
            if other != player:
                others = others.union(achievements[other])
        only = achievements[player].difference(others)
        print(f"Only {player} has: {only}")

    print()

    for player in players:
        missing = all_distinct.difference(achievements[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    achievement_tracker()
    print("\n=== End of Program ===")
