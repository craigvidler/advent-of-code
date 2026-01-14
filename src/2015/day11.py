"""
--- Day 11: Corporate Policy ---
https://adventofcode.com/2015/day/11

Not super efficient, but it works.
"""

from aocd import data as original
from more_itertools import sliding_window as sw

VALID_CHARS = 'abcdefghjkmnpqrstuvwxyz'  # no i, l or o
BASE = len(VALID_CHARS)
PW_LENGTH = len(original)


def decode(s):
    # treating a string as a base-BASE number (with digits VALID_CHARS),
    # convert to decimal, eg abcdefgh -> 161799556
    return sum(VALID_CHARS.index(c) * BASE ** i for i, c in enumerate(s[::-1]))


def encode(n):
    # convert a decimal int to base-BASE using VALID_CHARS as digits,
    # eg 161799556 -> abcdefgh
    out = []
    for i in range(PW_LENGTH - 1, -1, -1):
        q, n = divmod(n, BASE ** i)
        out.append(VALID_CHARS[q])
    return ''.join(out)


def increment(password):
    n = decode(password)
    while True:
        n += 1
        password = encode(n)
        if validate(password):
            return password


def validate(password):
    # test for two different pairs and a straight of three
    return (
        len({c1 for c1, c2 in sw(password, 2) if c1 == c2}) >= 2 and
        any(''.join(triplet) in VALID_CHARS for triplet in sw(password, 3))
    )


if __name__ == '__main__':
    p1_password = increment(original)
    p2_password = increment(p1_password)
    print('Part 1:', p1_password)
    print('Part 2:', p2_password)
