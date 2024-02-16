"""
--- Day 6: Custom Customs ---
https://adventofcode.com/2020/day/6
"""

from aocd import data


def parse(data):
    return [
        [set(line) for line in group.splitlines()]
        for group in data.split('\n\n')
    ]


def count(op, groups):
    return sum(len(op(*group)) for group in groups)


if __name__ == '__main__':
    groups = parse(data)
    print('Part 1:', count(set.union, groups))
    print('Part 2:', count(set.intersection, groups))
