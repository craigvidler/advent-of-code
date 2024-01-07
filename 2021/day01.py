"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1

Two shared numbers cancel out need for sliding window in part 2
"""

from aocd import data


def parse(data):
    return [int(n) for n in data.splitlines()]


def solve(numbers, interval=1):
    return sum(b > a for a, b in zip(numbers, numbers[interval:]))


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', solve(parsed))
    print('Part 2:', solve(parsed, 3))
