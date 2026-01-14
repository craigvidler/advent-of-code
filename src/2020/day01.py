"""
--- Day 1: Report Repair ---
https://adventofcode.com/2020/day/1
"""

from math import prod
from aocd import data

TARGET = 2020


def find(numbers, target=TARGET):
    complements = {}
    for n in numbers:
        if n in complements:
            return n, complements[n]
        complements[target - n] = n


def parse(data):
    return [int(n) for n in data.splitlines()]


def part1(numbers):
    return prod(find(numbers))


def part2(numbers):
    for n in numbers:
        if other_two := find(numbers, TARGET - n):
            return n * prod(other_two)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
