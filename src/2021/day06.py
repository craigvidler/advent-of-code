"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6

COULDDO: use list not dict
"""

from collections import Counter, defaultdict
from aocd import data


def simulate(fish, days):
    for _ in range(days):
        spawning = fish[0]
        for i in range(9):
            fish[i] = fish[i + 1]
        fish[6] += spawning
        fish[8] += spawning
    return sum(fish.values())


def parse(data):
    c = Counter(int(n) for n in data.split(','))
    return defaultdict(int, c)


if __name__ == '__main__':
    fish = parse(data)
    print('Part 1:', simulate(fish, 80))
    print('Part 2:', simulate(fish, 256))
