"""
--- Day 6: Trash Compactor ---
https://adventofcode.com/2025/day/6

`parse` transforms eg:
123 328  51 64              [[('1', ' ', ' '), ('2', '4', ' '), ('3', '5', '6')],
 45 64  387 23      ->       [('3', '6', '9'), ('2', '4', '8'), ('8', ' ', ' ')],
  6 98  215 314              [(' ', '3', '2'), ('5', '8', '1'), ('1', '7', '5')],
                             [('6', '2', '3'), ('4', '3', '1'), (' ', ' ', '4')]]

The input data is transposed (rows -> cols) to allow splitting at each "all
spaces" column into cells. These cells come grouped into column form (an
artefact of the splitting process), which is handy for p2 but which need to be
transposed back to grouped by row form for p1. `split_at` wrapped by `list` to
avoid exhausting generator since cells iterated over twice.
"""

from itertools import zip_longest as zip_l
from math import prod

from aocd import data
from more_itertools import split_at


def parse(data):
    lines = data.splitlines()
    ops = [sum if op == "+" else prod for op in lines.pop().split()]
    cells = list(split_at(zip_l(*lines, fillvalue=" "), lambda x: set(x) == {" "}))
    return ops, cells


def calculate(ops, cells):
    return sum(op(cell) for op, cell in zip(ops, cells))


if __name__ == "__main__":
    ops, cells = parse(data)

    p1_cells = ((int("".join(row)) for row in zip(*cell)) for cell in cells)
    p2_cells = ((int("".join(col)) for col in cell) for cell in cells)

    print("Part 1:", calculate(ops, p1_cells))
    print("Part 2:", calculate(ops, p2_cells))
