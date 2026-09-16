#!/usr/bin/env python3
"""ft_inventory_system.py: parse and analyze a game inventory from argv."""


import sys


def parse_inventory() -> dict[str, int]:
    """Parse 'name:quantity' arguments into a validated inventory dict."""
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        name, qty = parts
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")
    return inventory


def inventory_system() -> None:
    """Build an inventory from argv and report stats about it."""
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory()
    if len(inventory) == 0:
        print("Got inventory: {}")
    else:
        total_item = len(inventory)
        total_qty = sum(inventory.values())
        keys = list(inventory.keys())
        most = keys[0]
        least = keys[0]

        print(f"Got inventory: {inventory}")
        print(f"Item list: {list(inventory.keys())}")
        print(f"Total quantity of the {total_item} items: {total_qty}")

        for item in keys:
            percent = round(inventory[item] / total_qty * 100, 1)
            print(f"Item {item} represents {percent}%")
            if inventory[item] > inventory[most]:
                most = item
            if inventory[item] < inventory[least]:
                least = item
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")

        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    inventory_system()
    print("\n=== End of Program ===")
