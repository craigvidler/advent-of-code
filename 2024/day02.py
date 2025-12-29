"""
--- Day 2: Red-Nosed Reports ---
https://adventofcode.com/2024/day/2
"""

from itertools import pairwise

from aocd import data


def check_safe(report, dampener=False):
    if not dampener:
        return is_safe(report)
    return any(is_safe(report[:i] + report[i + 1 :]) for i, _ in enumerate(report))


def is_safe(report):
    steps = [a - b for a, b in pairwise(report)]
    return all(0 < s <= 3 for s in steps) or all(-3 <= s < 0 for s in steps)


if __name__ == "__main__":
    reports = [[int(n) for n in line.split()] for line in data.splitlines()]
    print("Part 1:", sum(check_safe(report) for report in reports))
    print("Part 2:", sum(check_safe(report, dampener=True) for report in reports))
