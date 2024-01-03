"""
--- Day 3: Spiral Memory ---
https://adventofcode.com/2017/day/3
"""

from math import ceil
from aocd import data


def part1(n):
    # Each tier has the square of each successive odd number at its bottom
    # right corner, which is the basis for locating n. `ceil_root` is the
    # next odd number above sqrt(n).

    ceil_root = ceil(n ** 0.5)
    ceil_root = ceil_root + 1 if ceil_root % 2 == 0 else ceil_root
    side = ceil_root - 1
    tier = ceil_root // 2
    dist_to_corner = (ceil_root ** 2 - n) % side
    dist_to_middle = abs(dist_to_corner - (side // 2))
    return dist_to_middle + tier


def part2(n):
    # Set value to sum of neighbours; add position and value to path;
    # move; if destination unoccupied, rotate left; return when value > n.

    LEFT_TURN = 1j
    NEIGHBOUR_OFFSETS = (-1 + 1j, 1j, 1 + 1j, -1, 0, 1, - 1 - 1j, -1j, 1 - 1j)
    orientation = 1  # facing right
    position = 0
    value = 1
    path = {position: value}

    while value <= n:
        value = sum(path.get(neighbour, 0) for neighbour in
                    [position + offset for offset in NEIGHBOUR_OFFSETS])
        path[position] = value
        position += orientation
        if position + orientation * LEFT_TURN not in path:
            orientation *= LEFT_TURN
    return value


if __name__ == '__main__':
    n = int(data)
    print('Part 1:', part1(n))
    print('Part 2:', part2(n))
