"""
--- Day 4: Repose Record ---
https://adventofcode.com/2018/day/4
"""

from collections import defaultdict, Counter
from types import SimpleNamespace as sns
from aocd import data
import parse as p


def parse(data):
    """Parse data, sort by timestamp."""
    pattern = p.compile('[{timestamp:ti}] {event}')
    unsorted = [sns(**pattern.parse(line).named) for line in data.splitlines()]
    return sorted(unsorted, key=lambda x: x.timestamp)


def prep(parsed):
    """
    Build two mappings: each guard -> every minute they've slept; minutes of
    the hour -> every time each guard has slept during that minute.
    """
    guards = minutes = defaultdict(list)
    guard = start = end = None
    pattern = p.compile('Guard #{id:d} begins shift')

    for line in parse(data):
        if parsed_line := pattern.parse(line.event):
            guard = parsed_line['id']
        elif line.event == 'falls asleep':
            start = line.timestamp.minute
        elif line.event == 'wakes up':
            end = line.timestamp.minute

            for minute in range(start, end):
                guards[guard].append(minute)
                minutes[minute].append(guard)

    return guards, minutes


def part1(guards):
    """
    Find the guard with the most minutes asleep, find the most frequent of
    those minutes, multiply that minute with the guard's id.
    """
    guard, minutes = max(guards.items(), key=lambda x: len(x[1]))
    return guard * max(minutes, key=minutes.count)


def part2(minutes):
    """
    For each minute find the highest number of records of each guard sleeping
    during that minute. Compare these maximums and find the maximum of
    maximums. Multiply the corresponding guard id and minute.
    """
    _, guard, minute = max(
        (frequency, guard, minute)
        for minute, guards in minutes.items()
        for guard, frequency in Counter(guards).most_common(1)
    )
    return guard * minute


if __name__ == '__main__':
    guards, minutes = prep(data)
    print('Part 1:', part1(guards))
    print('Part 2:', part2(minutes))
