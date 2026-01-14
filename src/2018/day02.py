"""
--- Day 2: Inventory Management System ---
https://adventofcode.com/2018/day/2
"""

from collections import Counter
from itertools import combinations
from aocd import data


def part1(lines):
    twos = threes = 0
    for line in lines:
        c = Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return twos * threes


def part2(lines):
    for word1, word2 in combinations(lines, 2):
        in_common = ''.join(char1 for char1, char2 in zip(word1, word2) if char1 == char2)
        if len(in_common) == len(word1) - 1:
            return in_common


if __name__ == '__main__':
    lines = data.splitlines()
    print('Part 1:', part1(lines))
    print('Part 2:', part2(lines))
