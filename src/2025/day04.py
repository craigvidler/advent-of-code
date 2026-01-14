"""
--- Day 4: Printing Department ---
https://adventofcode.com/2025/day/4
"""

from aocd import data

OFFSETS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def parse(data):
    return [[c == "@" for c in row] for row in data.splitlines()]


def remove(grid):
    # count then remove: both in one go would cause problems
    total = 0
    removals = []

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col and sum(neighbors(r, c, grid)) < 4:
                total += 1
                removals.append((r, c))

    for r, c in removals:
        grid[r][c] = 0

    return total


def neighbors(r, c, grid):
    # Don't like that the `len`s get calculated on every call, but NBD. Also,
    # least worst option without a wider rethink.

    for r_offset, c_offset in OFFSETS:
        row, col = r + r_offset, c + c_offset
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            yield grid[row][col]


if __name__ == "__main__":
    grid = parse(data)
    removal_counts = []

    # loop till `remove(grid)` returns 0
    while removed := remove(grid):
        removal_counts.append(removed)

    print("Part 1:", removal_counts[0])
    print("Part 2:", sum(removal_counts))
