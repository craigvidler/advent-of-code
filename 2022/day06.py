"""
--- Day 6: Tuning Trouble ---
https://adventofcode.com/2022/day/6
"""

from aocd import data
from more_itertools import sliding_window


def solve(windowsize=4):
    windows = sliding_window(data, windowsize)
    for i, window in enumerate(windows, windowsize):
        if len(set(window)) == windowsize:
            return i


if __name__ == '__main__':
    print('Part 1:', solve())
    print('Part 2:', solve(windowsize=14))
