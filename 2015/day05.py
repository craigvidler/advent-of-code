"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
https://adventofcode.com/2015/day/5
"""

from itertools import pairwise
from aocd import data


def parse(data):
    return [line for line in data.splitlines()]


def part1(words):
    return sum(
        all((
            len([c for c in word if c in 'aeiou']) >= 3,
            any(a == b for a, b, in pairwise(word)),
            all(a + b not in ['ab', 'cd', 'pq', 'xy'] for a, b in pairwise(word))
        ))
        for word in words
    )


def part2(words):
    return sum(
        all((
            any(word.count(a + b) > 1 for a, b in pairwise(word)),
            any(a == b for a, b in zip(word, word[2:])),
        ))
        for word in words
    )


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
