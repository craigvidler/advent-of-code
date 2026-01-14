"""
--- Day 2: Gift Shop ---
https://adventofcode.com/2025/day/2
"""

import re

from aocd import data

P1REGEX = re.compile(r"(\d+)\1")
P2REGEX = re.compile(r"(\d+)\1+")  # bosh


def parse(data):
    return [
        range(int(start), int(end) + 1)
        for start, end in [pair.split("-") for pair in data.split(",")]
    ]


def run(ranges, regex):
    return sum(n for r in ranges for n in r if regex.fullmatch(str(n)))


if __name__ == "__main__":
    ranges = parse(data)
    print("Part 1:", run(ranges, P1REGEX))
    print("Part 2:", run(ranges, P2REGEX))
