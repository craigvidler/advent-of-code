"""
--- Day 1: Chronal Calibration ---
https://adventofcode.com/2018/day/1
"""

from itertools import cycle
from aocd import data


def parse(data):
    return [int(n) for n in data.splitlines()]


def part1(numbers):
    return sum(numbers)


def part2(numbers):
    seen = set()
    running_total = 0
    for n in cycle(numbers):
        running_total += n
        if running_total in seen:
            return running_total
        seen.add(running_total)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
