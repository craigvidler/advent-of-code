"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""

from types import SimpleNamespace as sns
import parse as p
from aocd import data

DIRS = {'forward': 1, 'up': -1j, 'down': 1j}
STEP = p.compile('{dir} {n:d}')


def parse(data):
    return [sns(**STEP.parse(line).named) for line in data.splitlines()]


def part1(steps):
    summed = sum(DIRS[step.dir] * step.n for step in steps)
    return int(summed.real * summed.imag)


def part2(steps):
    pos = aim = 0
    for step in steps:
        if step.dir == 'forward':
            pos += step.n + (step.n * aim)
        else:
            aim += DIRS[step.dir] * step.n
    return int(pos.real * pos.imag)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
