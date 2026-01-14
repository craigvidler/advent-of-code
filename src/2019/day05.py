"""
--- Day 5: Sunny with a Chance of Asteroids ---
https://adventofcode.com/2019/day/5
"""

from aocd import data
from intcomputer import IntComputer


def parse(data):
    return [int(n) for n in data.split(',')]


def part1(program):
    return IntComputer(program, input_=1).run()


def part2(program):
    return IntComputer(program, input_=5).run()


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed.copy()))
    print('Part 2:', part2(parsed))
