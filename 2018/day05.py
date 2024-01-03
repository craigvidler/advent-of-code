"""
--- Day 5: Alchemical Reduction ---
https://adventofcode.com/2018/day/5
"""

from string import ascii_lowercase as atoz
from aocd import data


def react(polymer):
    out = []
    for char in polymer:
        out.pop() if out and out[-1] == char.swapcase() else out.append(char)
    return out


def part1(polymer):
    return len(react(polymer))


def part2(polymer):
    shortest = len(polymer)
    for char in atoz:
        edited = polymer.replace(char, '').replace(char.upper(), '')
        shortest = min(len(react(edited)), shortest)
    return shortest


if __name__ == '__main__':
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
