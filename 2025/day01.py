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
    # bruteforce: just step one number at a time, check and total as appropriate.
    p1_total = p2_total = 0

    for step in steps:
        dir = -1 if step < 0 else 1

        for _ in range(0, step, dir):
            pointer += dir
            p2_total += pointer % DIALSIZE == 0

        pointer = pointer % DIALSIZE
        p1_total += pointer == 0

    return p1_total, p2_total


if __name__ == "__main__":
    steps = parse(data)
    p1, p2 = run(steps)
    print("Part 1:", p1)
    print("Part 2:", p2)
