"""
--- Day 8: Space Image Format ---
https://adventofcode.com/2019/day/8
"""

from advent_of_code_ocr import convert_array_6
from aocd import data
import numpy as np

WIDTH, HEIGHT = 25, 6


def first_visible(stack):
    for n in stack:
        if n != 2:
            return n


def parse(data):
    return np.array(list(data), dtype=int).reshape(-1, HEIGHT, WIDTH)


def part1(layers):
    layer = min(layers, key=lambda n: (n == 0).sum())
    return (layer == 1).sum() * (layer == 2).sum()


def part2(layers):
    # Consider the 3D array to be cols (width/x), rows (height/y) and stacks
    # (depth/z). (A 'stack' is a 1D vector along the Z axis, not a 'layer',
    # which is 2D and orthogonal to a stack.) Transpose and reshape so that
    # stacks become rows in a 2D matrix (HEIGHT * WIDTH) tall.
    stacks = layers.transpose(1, 2, 0).reshape(HEIGHT * WIDTH, -1)
    pixels = [first_visible(stack) for stack in stacks]
    image = np.array(pixels).reshape(HEIGHT, WIDTH)
    return convert_array_6(image, fill_pixel=1, empty_pixel=0)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
