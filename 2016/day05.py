"""
--- Day 5: How About a Nice Game of Chess? ---
https://adventofcode.com/2016/day/5

TODO: Speed up. As is, runs in ~30s on 2013 MacBook Air. Further improvements
would have to come from multiprocessing I think (a job for another day).
"""

from _md5 import md5
from aocd import data


def nexthash_(door_id, start=0):
    i = start
    prefix = md5(door_id.encode())
    while True:
        i += 1
        hash_ = prefix.copy()
        hash_.update(b'%d' % i)
        if hash_.hexdigest().startswith('00000'):
            return hash_.hexdigest(), i


def solve(door_id):
    p1 = ''
    p2 = list('********')
    remaining = set('01234567')
    i = 0
    while remaining:
        hash_, i = nexthash_(door_id, i)
        if len(p1) < 8:
            p1 += hash_[5]
        if hash_[5] in remaining:
            p2[int(hash_[5])] = hash_[6]
            remaining.remove(hash_[5])
    return p1, ''.join(p2)


if __name__ == '__main__':
    p1, p2 = solve(data)
    print('Part 1: ', p1)
    print('Part 2: ', p2)
