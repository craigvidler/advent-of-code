"""
--- Day 4: Security Through Obscurity ---
https://adventofcode.com/2016/day/4
"""

from collections import Counter
from string import ascii_lowercase as atoz
from types import SimpleNamespace as sns
from aocd import data
import parse as p


def checksum(room):
    # note `-`, tallies sorted in descending order
    c = Counter(room.name.replace('-', ''))
    top5 = sorted(c.items(), key=lambda x: (-x[1], x[0]))[:5]
    return ''.join(letter for letter, _ in top5) == room.checksum


def decrypt(name, sector):
    return ''.join(
        ' ' if char == '-' else
        atoz[(sector + atoz.index(char)) % 26]
        for char in name
    )


def parse(data):
    pattern = p.compile('{name}-{sector:d}[{checksum}]')
    return [sns(**pattern.parse(line).named) for line in data.splitlines()]


def part1(rooms):
    return sum(room.sector for room in rooms if checksum(room))


def part2(rooms):
    for room in rooms:
        if 'north' in decrypt(room.name, room.sector):
            return room.sector


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
