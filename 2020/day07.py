"""
--- Day 7: Handy Haversacks ---
https://adventofcode.com/2020/day/7
"""

from collections import defaultdict
from aocd import data
import parse as p

MY_BAG = 'shiny gold'


def parse(data):
    # `by_children` maps each outer/parent bag type given on the left to its
    # list of inner/child bag types and quantities on the right. `by_parent`
    # maps each inner/child bag type on the right to a list of all
    # outer/parent bag types from the left in which it appears.
    by_children, by_parents = defaultdict(list), defaultdict(set)

    for line in data.splitlines():
        parent, children_chunk = line.split(' bags contain ')
        children = p.findall('{:d} {} bag', children_chunk)

        for child in children:
            # child[0] = quantity, child[1] = bag type
            by_children[parent].append((child[1], child[0]))
            by_parents[child[1]].add(parent)

    return by_children, by_parents


def part1():
    return len(rparents({MY_BAG}))


def part2():
    return sum(rchildren(*child) for child in by_children[MY_BAG])


def rparents(bags):
    res = set()
    for bag in bags:
        if bag in by_parents:
            res |= by_parents[bag] | rparents(by_parents[bag])
    return res


def rchildren(bag, count):
    if bag in by_children:
        return count + sum(count * rchildren(*child) for child in by_children[bag])
    return count


if __name__ == '__main__':
    by_children, by_parents = parse(data)
    print('Part 1:', part1())
    print('Part 2:', part2())
