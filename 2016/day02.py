"""
--- Day 2: Bathroom Security ---
https://adventofcode.com/2016/day/2

TODO: hardcoding the offset->key mappings like this is a quick and dirty
solution: will leave as is for now, but would be nicer to generate them
dynamically from the keypad strings supplied.
"""

from aocd import data


KEYPAD_A = {
    (-1 + 1j): '1', (0 + 1j): '2', (1 + 1j): '3',
    (-1 + 0j): '4', (0 + 0j): '5', (1 + 0j): '6',
    (-1 + -1j): '7', (0 + -1j): '8', (1 + -1j): '9'
}

KEYPAD_B = {
    (0 + 2j): '1',
    (-1 + 1j): '2', (0 + 1j): '3', (1 + 1j): '4',
    (-2 + 0j): '5', (-1 + 0j): '6', (0 + 0j): '7', (1 + 0j): '8', (2 + 0j): '9',
    (-1 + -1j): 'A', (0 + -1j): 'B', (1 + -1j): 'C',
    (0 + -2j): 'D'
}

DIRS = {'U': 1j, 'R': 1, 'D': -1j, 'L': -1}


def parse(data):
    return [[DIRS[c] for c in line] for line in data.splitlines()]


def solve(lines, keypad):
    out = ''
    position = 0
    for line in lines:
        for step in line:
            if position + step in keypad:
                position += step
        out += keypad[position]
    return out


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', solve(parsed, KEYPAD_A))
    print('Part 2:', solve(parsed, KEYPAD_B))
