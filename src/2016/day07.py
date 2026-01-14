"""
--- Day 7: Internet Protocol Version 7 ---
https://adventofcode.com/2016/day/7
"""

import re
from aocd import data
from more_itertools import sliding_window as sw


def parse(data):
    in_brackets = r'\[(\w+)\]'
    return [(
        re.sub(in_brackets, '.', line),  # supernet, outside brackets
        '.'.join(re.findall(in_brackets, line))  # hypernet, inside brackets
    ) for line in data.splitlines()]


def has_abba(s):
    return any(a == d and b == c and a != b for a, b, c, d in sw(s, 4))


def part1(lines):
    return sum(
        has_abba(supernet) and not has_abba(hypernet)
        for supernet, hypernet in lines
    )


def part2(lines):
    total = 0
    for supernet, hypernet in lines:
        babs = {(b, a, b) for a, b, c in sw(supernet, 3) if a == c and a != b}
        total += any((triplet in babs) for triplet in sw(hypernet, 3))
    return total


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
