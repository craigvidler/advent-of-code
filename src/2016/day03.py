"""
--- Day 3: Squares With Three Sides ---
https://adventofcode.com/2016/day/3
"""

from aocd import data
from itertools import batched, chain


def parse(data):
    return [[int(n) for n in line.split()] for line in data.splitlines()]


def part1(triangles):
    return sum(
        a < b + c and b < a + c and c < a + b
        for a, b, c in triangles
    )


def part2(lines):
    return part1(batched(chain(*zip(*lines)), 3))


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
