"""
--- Day 4: Camp Cleanup ---
https://adventofcode.com/2022/day/4
"""

from aocd import data
import parse as p


def parse(data):
    """parse the starts and ends of two ranges in each line"""
    PATTERN = p.compile('{:d}-{:d},{:d}-{:d}')
    return [PATTERN.parse(line) for line in data.splitlines()]


def prep(data):
    """take each pair of ranges and create a tuple of sets sorted by size"""
    return [
        sorted((set(range(a1, a2 + 1)), set(range(b1, b2 + 1))), key=len)
        for a1, a2, b1, b2 in parse(data)
    ]


def part1(assignment_pairs):
    """total pairs where a is a subset of b"""
    return sum(a <= b for a, b in assignment_pairs)


def part2(assignment_pairs):
    """total pairs where a and b intersect (overlap)"""
    return sum(1 for a, b in assignment_pairs if a & b)


if __name__ == '__main__':
    prepped = prep(data)
    print('Part 1:', part1(prepped))
    print('Part 2:', part2(prepped))
