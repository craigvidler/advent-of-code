"""
--- Day 3: No Matter How You Slice It ---
https://adventofcode.com/2018/day/3
"""

from collections import defaultdict
from types import SimpleNamespace as sns
from aocd import data
import parse as p


def parse(data):
    compiled = p.compile('#{id:d} @ {col:d},{row:d}: {width:d}x{height:d}')
    return [sns(**compiled.parse(line).named) for line in data.splitlines()]


def prep(data):
    fabric = defaultdict(list)
    for claim in parse(data):
        for x in range(claim.row, claim.row + claim.height):
            for y in range(claim.col, claim.col + claim.width):
                fabric[(x, y)].append(claim.id)
    return fabric


def part1(fabric):
    return sum(len(ids) > 1 for ids in fabric.values())


def part2(fabric):
    # A single loop should be faster than iterating twice for two set comps,
    # but I couldn't see a time difference in practice, and this is neater.
    all_ids = {claim_id for ids in fabric.values() for claim_id in ids}
    overlapping_ids = {
        claim_id for ids in fabric.values() if len(ids) > 1 for claim_id in ids
    }
    [non_overlapping] = all_ids.difference(overlapping_ids)
    return non_overlapping


if __name__ == '__main__':
    fabric = prep(data)
    print('Part 1:', part1(fabric))
    print('Part 2:', part2(fabric))
