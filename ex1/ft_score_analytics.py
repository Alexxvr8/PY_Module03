#!/usr/bin/env python3
"""ft_score_analytics: process command-line scores and compute basic stats"""


import sys


def score_analytics() -> None:
    """Filter valid scores from sys.argv and display basic statistics."""
    print("=== Player Score Analytics ===")
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}\n"
              f"Total players: {len(scores)}\n"
              f"Total score: {sum(scores)}\n"
              f"Average score: {sum(scores)/len(scores)}\n"
              f"High score: {max(scores)}\n"
              f"Low score: {min(scores)}\n"
              f"Score range: {max(scores)-min(scores)}")


if __name__ == "__main__":
    score_analytics()
    print("\n=== End of Program ===")
