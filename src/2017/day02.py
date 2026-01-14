"""
--- Day 2: Corruption Checksum ---
https://adventofcode.com/2017/day/2
"""

from aocd import data


def parse(data):
    return [[int(n) for n in line.split()] for line in data.splitlines()]


def part1(lines):
    return sum(max(line) - min(line) for line in lines)


def part2(lines):
    """find a, b in each line where a % b == 0, sum quotients"""
    total = 0
    for line in lines:
        for i, num1 in enumerate(line):
            for num2 in line[i + 1:]:
                q, r = divmod(*sorted([num1, num2], reverse=True))
                if not r:
                    total += q
                    break
    return total


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
