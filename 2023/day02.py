"""
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
"""

from collections import defaultdict
from math import prod
import re
from aocd import data


def parse(data):
    CUBES = re.compile(r'(\d+) (\w+)')
    return [[(color, int(n)) for n, color in CUBES.findall(line)]
            for line in data.splitlines()]


def part1(games):
    LIMITS = {'red': 12, 'green': 13, 'blue': 14}
    return sum(
        i for i, game in enumerate(games, 1)
        if all(n <= LIMITS[color] for color, n in game)
    )


def part2(games):
    total = 0
    for game in games:
        maxs = defaultdict(int)
        for color, n in game:
            maxs[color] = max(maxs[color], n)
        total += prod(maxs.values())
    return total


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
