"""
--- Day 3: Lobby ---
https://adventofcode.com/2025/day/3
"""

from aocd import data


def parse(data):
    return [[int(c) for c in line] for line in data.splitlines()]


def calculate(rows, slotcount):
    total = 0
    window = len(rows[0]) - slotcount + 1

    for row in rows:
        slots = [0] * slotcount
        start = 0

        for slot in range(slotcount):
            for i, n in enumerate(row[start : slot + window], start):
                if n > slots[slot]:
                    slots[slot] = n
                    start = i + 1

        total += int("".join(str(slot) for slot in slots))

    return total


if __name__ == "__main__":
    parsed = parse(data)
    print("Part 1:", calculate(parsed, 2))
    print("Part 2:", calculate(parsed, 12))
