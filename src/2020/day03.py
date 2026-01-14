"""
--- Day 3: Toboggan Trajectory ---
https://adventofcode.com/2020/day/3
"""

from math import prod
from aocd import data

SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


class Position:
    def __init__(self, x, y, max_x):
        self.x = x
        self.y = y
        self.max_x = max_x

    def __add__(self, slope):
        self.x = (self.x + slope[0]) % self.max_x  # wrap around
        self.y += slope[1]
        return self


def count_trees(treemap, slope):
    pos = Position(0, 0, len(treemap[0]))
    total = 0
    while pos.y < len(treemap):
        total += treemap[pos.y][pos.x] == '#'
        pos += slope
    return total


def part1(treemap):
    return count_trees(treemap, slope=SLOPES[1])


def part2(treemap):
    return prod(count_trees(treemap, slope) for slope in SLOPES)


if __name__ == '__main__':
    parsed = data.splitlines()
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
