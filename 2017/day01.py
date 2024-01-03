"""
--- Day 1: Inverse Captcha ---
https://adventofcode.com/2017/day/1
"""

from aocd import data


def part1(data):
    return sum(int(a) for a, b in zip(data, data[1:] + data[0]) if a == b)


def part2(data):
    length = len(data)
    offset = length // 2
    return sum(int(n) for i, n in enumerate(data) if n == data[(i + offset) % length])


if __name__ == '__main__':
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
