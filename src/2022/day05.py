"""
--- Day 5: Supply Stacks ---
https://adventofcode.com/2022/day/5
"""

from copy import deepcopy
from itertools import zip_longest
from aocd import data
import parse as p


def parse(data):
    stacks_text, steps_text = data.split('\n\n')

    # stacks: given example now {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    reversed_cols = zip_longest(*stacks_text.splitlines()[::-1])
    stacks = {
        int(col[0]): [i for i in col[1:] if i.isupper()]
        for col in reversed_cols if col[0].isdigit()
    }

    # steps: given example now [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
    STEPS_PATTERN = p.compile('move {:d} from {:d} to {:d}')
    steps = [STEPS_PATTERN.parse(line).fixed for line in steps_text.splitlines()]

    return stacks, steps


def do_moves(stacks, steps, lifo=False):
    # for part 1, reverse slice to emulated repeat popping
    step = -1 if lifo else None
    for moves, source, dest in steps:
        stacks[dest] += stacks[source][-moves:][::step]
        del stacks[source][-moves:]
    return ''.join(stack[-1] for stack in stacks.values())


if __name__ == '__main__':
    # need to deepcopy stacks (a dict of lists) to do two sets of operations on it
    stacks, steps = parse(data)
    print('Part 1:', do_moves(deepcopy(stacks), steps, lifo=True))
    print('Part 2:', do_moves(stacks, steps))
