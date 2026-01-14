"""
--- Day 7: The Sum of Its Parts ---
https://adventofcode.com/2018/day/7
"""

from collections import defaultdict
from copy import deepcopy
from heapq import heappop, heappush
from aocd import data

BASE_TTC = 60
TTC = {c: BASE_TTC + i for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)}


def preprocess(data):
    # `deps` maps steps to their pre-requisite steps. If a step has no
    # pre-requisites it has no key in deps and goes in `available`, otherwise
    # it goes in `pending` as well as a having a key in `deps`.
    steps = set()
    deps = defaultdict(set)

    for line in data.splitlines():
        dependency, dependent = line[5], line[36]
        steps |= {dependency, dependent}
        deps[dependent].add(dependency)

    pending = set(deps)
    available = sorted(steps - pending)
    return available, pending, deps


def part1(steps):
    steps, _ = assemble(*steps)
    return steps


def part2(steps):
    _, elapsed = assemble(*steps, max_workers=5, timed=True)
    return elapsed


def assemble(available, pending, deps, max_workers=1, timed=False):
    # Four stages: pending -> available -> working -> completed
    working = {}
    completed = []
    elapsed = 0

    while working or available:
        # transfer available -> working
        while len(working) < max_workers and available:
            step = heappop(available)  # handles alphabetic ordering
            working[step] = TTC[step]

        # transfer working -> completed
        for step, _ in list(working.items()):
            working[step] -= 1
            if working[step] == 0 or not timed:
                completed.append(step)
                del working[step]

        # transfer pending -> available
        completed_set = set(completed)
        for step in pending.copy():
            if deps[step] <= completed_set:  # all deps met
                heappush(available, step)
                pending.discard(step)

        elapsed += 1

    return ''.join(completed), elapsed


if __name__ == '__main__':
    steps = preprocess(data)
    # fresh copies of `available` and `pending` for Part 2
    print('Part 1:', part1(deepcopy(steps)))
    print('Part 2:', part2(steps))
