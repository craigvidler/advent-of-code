"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""

from aocd import data


def parse(data):
    return [1 if c == '(' else -1 for c in data]


def part1(parsed):
    return sum(parsed)


def part2(parsed):
    floor = 0
    for i, step in enumerate(parsed, 1):
        floor += step
        if floor < 0:
            return i


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
