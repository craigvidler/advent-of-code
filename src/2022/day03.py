"""
--- Day 3: Rucksack Reorganization ---
https://adventofcode.com/2022/day/3
"""

from itertools import batched
from string import ascii_letters
from aocd import data

PRIORITIES = {char: i for i, char in enumerate(ascii_letters, 1)}


def parse(data):
    return data.splitlines()


def part1(rucksacks):
    total = 0
    for rucksack in rucksacks:
        midpoint = len(rucksack) // 2
        [shared] = set(rucksack[:midpoint]) & set(rucksack[midpoint:])
        total += PRIORITIES[shared]
    return total


def part2(rucksacks):
    total = 0
    for a, b, c in batched(rucksacks, 3):
        [badge] = set(a) & set(b) & set(c)
        total += PRIORITIES[badge]
    return total


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
