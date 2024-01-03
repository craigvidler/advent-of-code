"""
--- Day 4: High-Entropy Passphrases ---
https://adventofcode.com/2017/day/4
"""

from aocd import data


def parse(data):
    return [line.split() for line in data.splitlines()]


def part1(lines):
    # count all lines where all words are unique
    return sum(len(line) == len(set(line)) for line in lines)


def part2(lines):
    # count all lines where all words are anagrammatically unique
    return sum(
        len(line) == len(set(tuple(sorted(word)) for word in line))
        for line in lines
    )


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
