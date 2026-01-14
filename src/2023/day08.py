"""
--- Day 8: Haunted Wasteland ---
https://adventofcode.com/2023/day/8

Part 2 too big to brute force. There are 6 nodes ending in 'A': for each, find
the number of steps till we reach the target node ending in 'Z'. On looking
for a pattern, these numbers turn out to be not prime as expected, but are
all <prime * prime common denominator>, a clue that the product of prime
factors (or just LCM) would yield the global period. (Watched Computerphile
(YouTube) on breaking Enigma last night, handy reminder about all this).
"""

from math import lcm
from itertools import cycle
from aocd import data


def navigate(steps, nodes, pos, stop):
    for i, step in enumerate(steps, 1):
        pos = nodes[pos][step]
        if pos.endswith(stop):
            return i


def parse(data):
    steps, nodes_chunk = data.split('\n\n')
    nodes = {
        line[:3]: {'L': line[7:10], 'R': line[12:15]}
        for line in nodes_chunk.splitlines()
    }
    return cycle(steps), nodes


def part1(steps, nodes, pos, stop):
    return navigate(steps, nodes, pos, stop)


def part2(steps, nodes, pos, stop):
    pos_list = [node for node in nodes if node.endswith(pos)]
    periods = [navigate(steps, nodes, pos, stop) for pos in pos_list]
    return lcm(*periods)


if __name__ == '__main__':
    steps, nodes = parse(data)
    print('Part 1:', part1(steps, nodes, pos='AAA', stop='ZZZ'))
    print('Part 2:', part2(steps, nodes, pos='A', stop='Z'))
