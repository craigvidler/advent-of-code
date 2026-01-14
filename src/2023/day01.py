"""
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1

Part 2 is tricky because the text numbers overlap. If I'd known the technique
below at the start, it would have saved a lot of frustration.
"""

import re
from aocd import data

# substitute but preserve overlapping letters
TRANS = {
    'zero': 'z0o',
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}


def part1(lines):
    numberset = [re.findall(r'\d', line) for line in lines]
    return sum(int(numbers[0] + numbers[-1]) for numbers in numberset)


def part2(lines):
    return part1([word2digit(line) for line in lines])


def word2digit(line):
    for word, digit in TRANS.items():
        line = line.replace(word, digit)
    return line


if __name__ == '__main__':
    parsed = data.splitlines()
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
