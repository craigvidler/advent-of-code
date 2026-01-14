"""
--- Day 9: All in a Single Night ---
https://adventofcode.com/2015/day/9
"""

from itertools import permutations
from aocd import data
from more_itertools import pairwise
import parse as p


def parse(data):
    PARSED = p.compile('{} to {} = {:d}')
    locations, distances = set(), {}
    for line in data.splitlines():
        a, b, dist = PARSED.parse(line)
        locations.update((a, b))
        distances[a, b] = distances[b, a] = dist
    return locations, distances


def all_routes(locations, distances):
    return [
        sum(distances[pair] for pair in pairwise(perm))
        for perm in unique_permutations(locations)
    ]


def unique_permutations(iterable):
    # `permutations` alone returns 'CBA' as well as 'ABC', we only need one.
    # (7! possibilities -> 7!/2)
    for perm in permutations(iterable):
        if perm[0] <= perm[-1]:
            yield perm


if __name__ == '__main__':
    locations, distances = parse(data)
    routes = all_routes(locations, distances)
    print('Part 1:', min(routes))
    print('Part 2:', max(routes))
