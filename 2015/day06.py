"""
--- Day 6: Probably a Fire Hazard ---
https://adventofcode.com/2015/day/6#part2
"""

from aocd import data
import numpy as np
import parse as p


def prep(action, x1, y1, x2, y2):
    return (action, slice(x1, x2 + 1), slice(y1, y2 + 1))


def parse(data):
    PARSER = p.compile('{} {:d},{:d} through {:d},{:d}')
    return [prep(*PARSER.parse(line)) for line in data.splitlines()]


def solve(steps):
    ROWS, COLS = 1000, 1000
    p1grid = np.zeros((ROWS, COLS), dtype=bool)
    p2grid = np.zeros((ROWS, COLS), dtype=np.int8)

    for action, rows, cols in steps:
        if action == 'turn on':
            p1grid[rows, cols] = True
            p2grid[rows, cols] += 1
        elif action == 'turn off':
            p1grid[rows, cols] = False
            p2grid[rows, cols] -= np.minimum(1, p2grid[rows, cols])
        else:
            p1grid[rows, cols] = ~p1grid[rows, cols]
            p2grid[rows, cols] += 2

    return p1grid.sum(), p2grid.sum()


if __name__ == '__main__':
    parsed = parse(data)
    p1, p2 = solve(parsed)
    print('Part 1:', p1)
    print('Part 2:', p2)
