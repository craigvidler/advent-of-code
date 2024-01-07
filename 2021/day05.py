"""
--- Day 5: Hydrothermal Venture ---
https://adventofcode.com/2021/day/5
"""

from collections import defaultdict
from itertools import zip_longest
from aocd import data
import parse as p


def orthogonal(endpoints):
    # if line is horiz/vert, return row/col it's on (if diag, return None)
    x1, y1, x2, y2 = endpoints
    if x1 == x2 or y1 == y2:
        return x1 if x1 == x2 else y1


def draw_line(endpoints):
    x1, y1, x2, y2 = endpoints
    xstep = 1 if x1 <= x2 else -1
    ystep = 1 if y1 <= y2 else -1

    # diagonals have equal x, y ranges; orthogonals need one filled
    return zip_longest(
        range(x1, x2 + xstep, xstep),
        range(y1, y2 + ystep, ystep),
        fillvalue=orthogonal(endpoints)
    )


def parse(data):
    pattern = p.compile('{:d},{:d} -> {:d},{:d}')
    return [pattern.parse(line) for line in data.splitlines()]


def solve(all_endpoints, orth_only=False):
    points = defaultdict(int)
    for endpoints in all_endpoints:
        # Skip if part1 and line is diagonal. NB 0 is a valid orthogonal.
        if orth_only and orthogonal(endpoints) is None:
            continue
        for point in draw_line(endpoints):
            points[point] += 1
    return sum(count > 1 for count in points.values())


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', solve(parsed, orth_only=True))
    print('Part 2:', solve(parsed))
