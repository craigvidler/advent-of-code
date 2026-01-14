"""
--- Day 2: 1202 Program Alarm ---
https://adventofcode.com/2019/day/2

TODO: Part 2 runs slow (~2-3s): IntComputer needs optimised
"""

from aocd import data
from intcomputer import IntComputer


def parse(data):
    return [int(n) for n in data.split(',')]


def part1(program, noun=12, verb=2):
    computer = IntComputer(program.copy())  # refresh data every run
    computer.program[1:3] = noun, verb
    computer.run()
    return computer.program[0]


def part2(program):
    TARGET = 19690720
    for noun in range(100):
        for verb in range(100):
            if part1(program, noun, verb) == TARGET:
                return 100 * noun + verb


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
