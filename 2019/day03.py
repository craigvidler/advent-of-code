"""
--- Day 3: Crossed Wires ---
https://adventofcode.com/2019/day/3
"""

from aocd import data


def manhattan(point):
    return int(abs(point.real) + abs(point.imag))


def plot_path(wire):
    DIRECTIONS = {'U': 1j, 'R': 1, 'D': -1j, 'L': -1}
    path = {}
    pos = i = 0
    for direction, distance in wire:
        for _ in range(distance):
            i += 1
            pos += DIRECTIONS[direction]
            if not path.get(pos, 0):
                path[pos] = i
    return path


def prep(parsed):
    return [plot_path(wire) for wire in parsed]


def parse(data):
    return (
        [(line[0], int(line[1:])) for line in wire.split(',')]
        for wire in data.splitlines()
    )


def part1(intersects):
    return min(manhattan(intersect) for intersect in intersects)


def part2(intersects):
    return min([path_a[point] + path_b[point] for point in intersects])


if __name__ == '__main__':
    path_a, path_b = prep(parse(data))
    intersects = path_a.keys() & path_b.keys()
    print('Part 1:', part1(intersects))
    print('Part 2:', part2(intersects))
