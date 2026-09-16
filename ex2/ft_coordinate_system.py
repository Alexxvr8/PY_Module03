#!/usr/bin/env python3
"""ft_coordinate_system: read 3D coordinates and compute euclidean distances"""


import math


def get_player_pos() -> tuple[float, float, float]:
    """Prompt for'x,y,z' coordinates, validate them and return a float tuple"""
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = text.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords = []
        error = False
        for p in parts:
            try:
                coords.append(float(p))
            except ValueError as e:
                print(f"Error on parameter '{p}': {e}")
                error = True
                break
        if error:
            continue
        return (coords[0], coords[1], coords[2])


def coordinate_system() -> None:
    """Read two 3D points and print the distance to center and between them."""
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    dist = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(dist, 4)}")

    print("Get a second set of coordinates")
    p2 = get_player_pos()
    dist = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    try:
        coordinate_system()
    except (EOFError, KeyboardInterrupt):
        print("\n\nProgram interrupted!!!")
    finally:
        print("\n=== End of Program ===")
