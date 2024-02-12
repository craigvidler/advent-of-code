"""
--- Day 8: Two-Factor Authentication ---
https://adventofcode.com/2016/day/8
"""

from advent_of_code_ocr import convert_array_6
from aocd import data
import numpy as np
import parse as p


def prep(command, rowcol, _, index, offset):
    target = (index, slice(None)) if rowcol == 'row' else (slice(None), index)
    return command, target, offset


def parse(data):
    RECTPARSER = p.compile('{} {:d}x{:d}')
    ROTPARSER = p.compile('{} {} {}={:d} by {:d}')
    out = []
    for line in data.splitlines():
        if line.startswith('rect'):
            out.append(RECTPARSER.parse(line))
        else:
            out.append(prep(*ROTPARSER.parse(line)))
    return out


def solve(steps):
    screen = np.zeros((6, 50), dtype=bool)
    for command, arg1, arg2 in steps:
        if command == 'rect':
            # arg2 = row, arg1 = col
            screen[:arg2, :arg1] = True
        else:
            # arg1 = (row, :) or (:, col), arg2 = offset
            screen[arg1] = np.roll(screen[arg1], arg2)
    return screen


if __name__ == '__main__':
    parsed = parse(data)
    screen = solve(parsed)
    print('Part 1:', screen.sum())
    print('Part 2:', convert_array_6(screen, fill_pixel=True, empty_pixel=False))
