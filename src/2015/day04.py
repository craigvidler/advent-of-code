"""
--- Day 4: The Ideal Stocking Stuffer ---
https://adventofcode.com/2015/day/4

After profiling this code and variations with `timeit`: _md5 faster than
hashlib (~25%); md5.copy() improves times ~5-10%; `b'%d' % i` faster than
`str(i).encode()` (~5%).
"""

from _md5 import md5
from aocd import data


def mine(key, zeroes, start):
    target = '0' * zeroes
    i = start
    prefix = md5(key.encode())
    while True:
        i += 1
        hash_ = prefix.copy()
        hash_.update(b'%d' % i)
        if hash_.hexdigest().startswith(target):
            return i


if __name__ == '__main__':
    p1 = mine(data, 5, 0)
    print('Part 1:', p1)
    p2 = mine(data, 6, p1 - 1)
    print('Part 2:', p2)
