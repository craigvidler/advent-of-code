"""
--- Day 1: Calorie Counting ---
https://adventofcode.com/2022/day/1
"""

from aocd import data


def parse(data):
    return [[int(n)for n in elf.split()] for elf in data.split('\n\n')]


def part1(elves):
    return max(sum(elf) for elf in elves)


def part2(elves):
    return sum(sorted(sum(elf) for elf in elves)[-3:])


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
