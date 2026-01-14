"""
--- Day 1: Historian Hysteria ---
https://adventofcode.com/2024/day/1
"""

from collections import Counter
from aocd import data


def preprocess(data):
    # two steps for readability: first parse, then transpose and sort
    parsed = [[int(n) for n in line.split()] for line in data.splitlines()]
    return [sorted(column) for column in zip(*parsed)]


def part1(preprocessed):
    # sum the differences between each pair of numbers going down the columns
    return sum(abs(left - right) for left, right in zip(*preprocessed))


def part2(preprocessed):
    # sum each number in the left column times its tally in the right
    left, right = preprocessed
    c = Counter(right)
    return sum(n * c[n] for n in left)


if __name__ == '__main__':
    preprocessed = preprocess(data)
    print('Part 1:', part1(preprocessed))
    print('Part 2:', part2(preprocessed))
