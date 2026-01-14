"""
--- Day 8: Treetop Tree House ---
https://adventofcode.com/2022/day/8

Runs a bit slow (prob numpy column manipulation in `get_sightlines`)
"""

from math import prod
from aocd import data
from more_itertools import takewhile_inclusive
import numpy as np


def parse(data):
    return np.array([[int(n) for n in line] for line in data.splitlines()])


def part1(all_sightlines):
    return sum(is_visible(tree, lines) for tree, lines in all_sightlines)


def part2(all_sightlines):
    return max(scenic_score(tree, lines) for tree, lines in all_sightlines)


def get_sightlines(trees):
    # Return each tree's height and its four sightlines (left, right, above,
    # below). To ease Part 2, order sightlines as they'd appear radiating out
    # from the tree's POV (ie left and above reversed).
    return [
        (tree, [trees[y, :x][::-1], trees[y, x + 1:],
                trees[:y, x][::-1], trees[y + 1:, x]])
        for y, row in enumerate(trees)
        for x, tree in enumerate(row)
    ]


def is_visible(tree, sightlines):
    # If we're on an edge, or there's a clear line of neighbours where all are
    # `< tree`, at least one sightline will be an empty list.
    return [] in [[n for n in line if n >= tree] for line in sightlines]


def scenic_score(tree, sightlines):
    # `takewhile_inclusive` with `< tree` gives all (smaller) numbers until we
    # hit a `n >= tree` (but also includes that `n`, unlike `takewhile`).
    # Count lengths of all scenic lines and return product.
    scenic_lines_counts = [
        len(list(takewhile_inclusive(lambda n: n < tree, line)))
        for line in sightlines
    ]
    return prod(scenic_lines_counts)


if __name__ == '__main__':
    trees = parse(data)
    all_sightlines = get_sightlines(trees)
    print('Part 1:', part1(all_sightlines))
    print('Part 2:', part2(all_sightlines))
