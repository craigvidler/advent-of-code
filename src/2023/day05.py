"""
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5
"""

from itertools import batched
from aocd import data


def parse(data):
    # Convert each mapping from `dest, source, range` to `range(source start,
    # source end), offset`
    seeds_chunk, *maps_chunk = data.split('\n\n')
    seeds = [int(n) for n in seeds_chunk[7:].split()]
    maps = []
    for map_chunk in maps_chunk:
        mapping = []
        for line in map_chunk.splitlines()[1:]:
            dest, source, offset = [int(n) for n in line.split()]
            mapping.append(((source, source + offset), dest - source))
        maps.append(mapping)
    return seeds, maps


def part1(seeds, maps):
    # convert individual seed values to ranges to share logic with part 2
    seed_ranges = [(seed, seed + 1) for seed in seeds]
    return process(seed_ranges, maps)


def part2(seeds, maps):
    seed_ranges = [(start, start + span) for start, span in batched(seeds, 2)]
    return process(seed_ranges, maps)


def process(ranges, maps):
    for map_ in maps:
        next_ranges = []
        for range_ in ranges:
            next_ranges.extend(process_step(range_, map_))
        ranges = next_ranges

    return min(range_start for range_start, _ in ranges)


def process_step(range_, map_):
    range_start, range_stop = range_
    if range_stop <= range_start:
        return []

    for (map_start, map_stop), offset in map_:
        # no overlap, nothing to do, check next span in `map_`
        if range_stop <= map_start or range_start >= map_stop:
            continue

        # `range_` completely within `map_`
        if map_start <= range_start < map_stop and map_start < range_stop <= map_stop:
            return [(range_start + offset, range_stop + offset)]

        # Overlap left, overlap right, or both. Recursion ensures
        # non-overlapping parts of `range_` are also checked against all
        # other spans in `map_`.
        return (
            process_step((range_start, map_start), map_)
            + [(max(range_start, map_start) + offset, min(range_stop, map_stop) + offset)]
            + process_step((map_stop, range_stop), map_)
        )

    # `range_` wasn't mapped at all
    return [(range_start, range_stop)]


if __name__ == '__main__':
    seeds, maps = parse(data)
    print('Part 1:', part1(seeds, maps))
    print('Part 2:', part2(seeds, maps))
