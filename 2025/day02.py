"""
--- Day 2: Gift Shop ---
https://adventofcode.com/2025/day/2
"""

import re

import parse as p
from aocd import data

P1REGEX = re.compile(r"(\d+)\1")
P2REGEX = re.compile(r"(\d+)\1+")  # bosh


def parse(data):
    pattern = p.compile("{:d}-{:d}")
    return [pattern.parse(pair) for pair in data.split(",")]


def run(ranges, regex):
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if m := regex.fullmatch(str(n)):
                total += int(m.group(0))
    return total


if __name__ == "__main__":
    ranges = parse(data)
    print("Part 1:", run(ranges, P1REGEX))
    print("Part 2:", run(ranges, P2REGEX))
