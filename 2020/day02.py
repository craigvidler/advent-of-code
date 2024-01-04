"""
--- Day 2: Password Philosophy ---
https://adventofcode.com/2020/day/2
"""

from aocd import data
import parse as p
from types import SimpleNamespace as sns


def parse(data):
    compiled = p.compile('{lower:d}-{upper:d} {letter}: {password}')
    return [sns(**compiled.parse(line).named) for line in data.splitlines()]


def part1(lines):
    return sum(
        l.lower <= l.password.count(l.letter) <= l.upper for l in lines
    )


def part2(lines):
    return sum(
        (l.password[l.lower - 1] + l.password[l.upper - 1]).count(l.letter) == 1
        for l in lines
    )


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
