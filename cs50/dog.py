"""
Dog Bus Tracker — simple interactive script for CS50-style exercise.

Behavior:
 - Maintains a bus dictionary keyed by seat number (int).
 - Each seat's value is a dict with: name, breed, pickup, dropoff.
 - Prints starting roster (seat, name, pickup time).
 - Adds one new pet if there's room (MAX_SEATS).
 - Removes a pet who leaves early (specified as argv or prompted).
 - Prints final roster showing remaining pets and dropoff times.

Usage:
 - Interactive: python dog.py
 - Non-interactive: python dog.py <NameToRemove>

The script is tolerant of non-tty runs: if no argv and stdin is not a TTY,
it will pick the first pet to leave automatically (useful for automated runs).
"""

from __future__ import annotations

import sys
from typing import Dict, Any

MAX_SEATS = 4


def print_roster(
    title: str, bus: Dict[int, Dict[str, Any]], show: str = "pickup"
) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    if not bus:
        print("(no passengers)")
        return
    for seat in sorted(bus.keys()):
        pet = bus[seat]
        time = pet.get(show + "_time", "N/A")
        print(
            f"Seat {seat}: {pet['name']} (pickup: {pet['pickup_time']}, dropoff: {pet['dropoff_time']})"
        )


def main(argv: list[str]) -> None:
    # 1. Start with a bus dictionary holding current passengers.
    bus: Dict[int, Dict[str, Any]] = {
        1: {
            "name": "Buddy",
            "breed": "Beagle",
            "pickup_time": "08:00",
            "dropoff_time": "16:00",
        },
        2: {
            "name": "Miso",
            "breed": "Shih Tzu",
            "pickup_time": "08:10",
            "dropoff_time": "15:50",
        },
        3: {
            "name": "Luna",
            "breed": "Labrador",
            "pickup_time": "08:20",
            "dropoff_time": "16:10",
        },
    }

    # 2. Print a starting roster showing each pet’s seat, name, and pickup time.
    print_roster("Starting roster (pickup times)", bus, show="pickup")

    # 3. Add one new pet if there's room on the bus.
    if len(bus) < MAX_SEATS:
        next_seat = max(bus.keys(), default=0) + 1
        new_pet = {
            "name": "Charlie",
            "breed": "Poodle",
            "pickup_time": "08:30",
            "dropoff_time": "16:20",
        }
        bus[next_seat] = new_pet
        print(f"\nPicked up new passenger: {new_pet['name']} in seat {next_seat}.")
    else:
        print("\nBus full — no new pickups.")

    print_roster("Roster after pickup", bus, show="pickup")

    # 4. Ask which pet leaves early.
    # Support: argv[1] to specify name non-interactively, otherwise prompt.
    names = [pet["name"] for seat, pet in sorted(bus.items())]

    leaving_name = None
    if len(argv) > 1:
        leaving_name = argv[1]
        print(f"\nRequested to remove: {leaving_name}")
    else:
        # If no stdin (non-interactive), pick first pet to leave
        try:
            if sys.stdin and sys.stdin.isatty():
                print("\nWhich pet leaves early? Available: " + ", ".join(names))
                leaving_name = input("Enter pet name: ").strip()
            else:
                # non-tty, choose first pet
                leaving_name = names[0] if names else None
                print(
                    f"\nNo interactive input available — defaulting to remove: {leaving_name}"
                )
        except Exception:
            leaving_name = names[0] if names else None

    removed = None
    if leaving_name:
        # find by name (case-insensitive)
        for seat, pet in list(bus.items()):
            if pet["name"].lower() == leaving_name.lower():
                removed = bus.pop(seat)
                print(f"\n{removed['name']} has headed home from seat {seat}.")
                break
        if removed is None:
            print(f"\nNo pet named '{leaving_name}' found on the bus.")
    else:
        print("\nNo pet specified to leave early.")

    # 5. Print a final roster listing the remaining pets and their dropoff times.
    print_roster("Final roster (dropoff times)", bus, show="dropoff")


if __name__ == "__main__":
    main(sys.argv)
