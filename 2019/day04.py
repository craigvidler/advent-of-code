"""
--- Day 4: Secure Container ---
https://adventofcode.com/2019/day/4
"""

from aocd import data
from more_itertools import pairwise


def parse(data):
    start, end = data.split('-')
    return [str(n) for n in range(int(start), int(end) + 1)]


def p1rules(n):
    return (
        any(a == b for a, b in pairwise(n)) and
        all(a <= b for a, b in pairwise(n))
    )


def p2rule(n):
    invalids = {c for c in n if n.count(c) > 2}
    return any(a == b for a, b in pairwise(n) if a not in invalids)


def validate(numbers):
    p1_total = p2_total = 0
    for n in numbers:
        if p1rules(n):
            p1_total += 1
            p2_total += p2rule(n)  # p2 only considered if p1 passed
    return p1_total, p2_total


if __name__ == '__main__':
    numbers = parse(data)
    p1_total, p2_total = validate(numbers)
    print('Part 1:', p1_total)
    print('Part 2:', p2_total)
