"""
--- Day 2: I Was Told There Would Be No Math ---
https://adventofcode.com/2015/day/2
"""

import parse as p
from aocd import data


def parse(data):
    pattern = p.compile('{:d}x{:d}x{:d}')
    return [pattern.parse(line) for line in data.splitlines()]


def part1(boxes):
    total = 0
    for w, h, l in boxes:
        area = 2 * (w * h + w * l + h * l)
        extra = min(l * w, w * h, h * l)
        total += area + extra
    return total


def part2(boxes):
    total = 0
    for w, h, l in boxes:
        volume = w * h * l
        smallest_perimeter = 2 * min(l + w, w + h, h + l)
        total += volume + smallest_perimeter
    return total


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
