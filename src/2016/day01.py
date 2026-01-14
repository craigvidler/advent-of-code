"""
--- Day 1: No Time for a Taxicab ---
https://adventofcode.com/2016/day/1
"""

from aocd import data


def parse(data):
    TURNS = {'L': 1j, 'R': -1j}
    return [(TURNS[step[0]], int(step[1:])) for step in data.strip().split(', ')]


def manhattan(position):
    return int(abs(position.real) + abs(position.imag))


def solve(steps, part2=False):
    orientation = 1j
    position = 0
    visited = {position}
    for turn, distance in steps:
        orientation *= turn
        for block in range(1, distance + 1):
            position += orientation
            if part2 and position in visited:
                return manhattan(position)
            visited.add(position)
    return manhattan(position)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', solve(parsed))
    print('Part 2:', solve(parsed, part2=True))
