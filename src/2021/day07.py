"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7

For Part 2, it's not enough just to use the rounded mean to find the target
position, which stumped me for a while. Complication explained here:
https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/
"""

import math
import statistics
from aocd import data


def triangular(n):
    return (n ** 2 + n) // 2  # returns nth triangular number


def sum_triangulars(mean, positions):
    return sum(triangular(abs(mean - p)) for p in positions)


def parse(data):
    return [int(n) for n in data.split(',')]


def part1(positions):
    median = round(statistics.median(positions))
    return sum(abs(median - p) for p in positions)


def part2(positions):
    mean = statistics.mean(positions)
    floor, ceil = math.floor(mean), math.ceil(mean)
    return min(sum_triangulars(floor, positions), sum_triangulars(ceil, positions))


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
