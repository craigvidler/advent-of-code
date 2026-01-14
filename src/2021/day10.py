"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""

from statistics import median
from aocd import data


def parse(data):
    return data.splitlines()


def score(lines):
    points = {'(': 1, '[': 2, '{': 3, '<': 4, ')': 3, ']': 57, '}': 1197, '>': 25137}
    p1_score = 0
    p2_scores = []

    for line in lines:
        stack = []
        for c in line:
            if c in '([{<':  # open bracket, record it on stack
                stack.append(c)
            elif stack.pop() + c not in '()[]{}<>':  # part 1, corrupted line
                p1_score += points[c]
                break
        else:  # part 2, not corrupted but incomplete line
            p2_score = 0
            for c in stack[::-1]:
                p2_score = p2_score * 5 + points[c]
            p2_scores.append(p2_score)

    return p1_score, median(p2_scores)


if __name__ == '__main__':
    parsed = parse(data)
    p1, p2 = score(parsed)
    print('Part 1:', p1)
    print('Part 2:', p2)
