"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---
https://adventofcode.com/2015/day/3
"""

from aocd import data


def parse(data):
    DIRS = {'^': 1j, '>': 1, 'v': -1j, '<': -1}
    return [DIRS[c] for c in data]


def visits(steps):
    pos = 0
    visited = {pos}
    for step in steps:
        pos += step
        visited.add(pos)
    return visited


def part1(steps):
    return len(visits(steps))


def part2(steps):
    santa = visits(steps[::2])
    robosanta = visits(steps[1::2])
    return len(santa | robosanta)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
