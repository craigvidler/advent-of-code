"""
--- Day 13: A Maze of Twisty Little Cubicles ---
https://adventofcode.com/2016/day/13
"""

from collections import deque
from aocd import data

FAVNUM = int(data)
START = (1, 1)
P1_END = (31, 39)
P2_LIMIT = 50


def bfs(start, end=None, limit=None):
    q = deque([start])
    previous = {}

    while q:
        current = q.popleft()

        if limit and path_length(current, start, previous) > limit:
            return len(previous)
        if end and current == end:
            return path_length(current, start, previous) - 1

        for neighbor in neighbors(*current):
            if neighbor not in previous:
                previous[neighbor] = current
                q.append(neighbor)


def neighbors(x, y):
    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        if nx >= 0 and ny >= 0 and is_passage(nx, ny):
            yield (nx, ny)


def is_passage(x, y):
    n = x * x + 3 * x + 2 * x * y + y + y * y + FAVNUM
    return n.bit_count() % 2 == 0


def path_length(node, start, previous):
    return 1 if node == start else 1 + path_length(previous[node], start, previous)


if __name__ == '__main__':
    print('Part 1:', bfs(START, P1_END))
    print('Part 2:', bfs(START, limit=P2_LIMIT))
