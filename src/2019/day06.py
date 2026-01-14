"""
--- Day 6: Universal Orbit Map ---
https://adventofcode.com/2019/day/6
"""

from aocd import data


def path(from_, to, orbits):
    path = []
    while from_ != to:
        from_ = orbits[from_]
        path.append(from_)
    return path


def parse(data):
    return {
        orbiting: orbited
        for line in data.splitlines()
        for orbited, orbiting in [line.split(')')]
    }


def part1(orbits):
    # totalling the steps from each object to COM gives all direct and
    # indirect orbits
    paths = [path(orbiting, 'COM', orbits) for orbiting in orbits]
    return sum(len(path) for path in paths)


def part2(orbits):
    # Creating a path from each to COM then removing the common elements
    # leaves the path between each other (actually, not exactly, but the
    # length is equivalent to the number of steps we want).
    you_to_com = path('YOU', 'COM', orbits)
    san_to_com = path('SAN', 'COM', orbits)
    return len(set(you_to_com) ^ set(san_to_com))


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
