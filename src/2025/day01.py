"""
--- Day 1: Secret Entrance ---
https://adventofcode.com/2025/day/1
"""

from aocd import data

START = 50
DIALSIZE = 100


def parse(data):
    return [
        int(line[1:]) if line[0] == "R" else -int(line[1:]) for line in data.split()
    ]


def run(steps, pointer=START):
    p1_total = p2_total = 0

    for step in steps:
        dir = -1 if step < 0 else 1

        q, r = divmod(step, DIALSIZE * dir)
        p2_total += q

        for _ in range(0, r, dir):
            pointer += dir
            p2_total += pointer % DIALSIZE == 0

        pointer %= DIALSIZE  # ensure we're brought back to 0-99
        p1_total += pointer == 0

    return p1_total, p2_total


if __name__ == "__main__":
    steps = parse(data)
    p1, p2 = run(steps)
    print("Part 1:", p1)
    print("Part 2:", p2)
