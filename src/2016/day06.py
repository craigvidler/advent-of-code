"""
--- Day 6: Signals and Noise ---
https://adventofcode.com/2016/day/6
"""

from aocd import data


def part1(lines):
    return ''.join(max(col, key=col.count) for col in zip(*data.split()))


def part2(lines):
    return ''.join(min(col, key=col.count) for col in zip(*data.split()))


if __name__ == '__main__':
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
