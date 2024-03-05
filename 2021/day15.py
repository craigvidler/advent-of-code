"""
--- Day 15: Chiton ---
https://adventofcode.com/2021/day/15

Version 2: much faster (~1.25s from ~3.75s, 2014 MacBook Air), mainly due to
no pre-computed big adjacency list in p2, neighbors found on the fly.

[see footnote]
"""

from heapq import heappop, heappush
from aocd import data
import numpy as np

START = (0, 0)
EXPANDBY = 5


def parse(data):
    parsed = [[n for n in line] for line in data.splitlines()]
    return np.array(parsed, dtype=np.int8)


def expand(p1_grid):
    def mod_increment(n, i): return (n + i - 1) % 9 + 1
    vstack = np.vstack([mod_increment(p1_grid, i) for i in range(EXPANDBY)])
    return np.hstack([mod_increment(vstack, i) for i in range(EXPANDBY)])


def dijkstra(grid):
    end = grid.shape[0] - 1, grid.shape[1] - 1
    pq = [(0, START)]
    visited = set()

    while pq:
        cost, current = heappop(pq)
        if current == end:
            return cost
        for neighbor in neighbors(*current, *end):
            if neighbor not in visited:
                visited.add(neighbor)
                heappush(pq, (cost + grid[neighbor], neighbor))


def neighbors(r, c, maxrow, maxcol):
    for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= row <= maxrow and 0 <= col <= maxcol:
            yield (row, col)


if __name__ == '__main__':
    p1_grid = parse(data)
    p2_grid = expand(p1_grid)
    print('Part 1:', dijkstra(p1_grid))
    print('Part 2:', dijkstra(p2_grid))


"""
Have experimented with A* instead of Dijkstra: slower (~2.5s). Was just using
manhattan distance as heuristic, which is prob not helpful in this case with
the importance of arbitrary weights superceding the importance of mere
distance, and a meandering best path. Also tried Euclidean, but too
computation-heavy. Maybe with a better heuristic A* could outperform
Dijkstra, but maybe it's simply not the best choice for this kind of
problem.

Briefly experimented with Dijkstra with a Fib Heap for pq and decrease-key
(ie eager vs the current lazy version of Dijkstra), but the results were very
slow (~14s) - some of that surely improvable with better implementation, but
again may be simply a case of being ill-suited to the task.

Numpy: could maybe improve `expand` with `np.tile` or `np.broadcast_to` etc
(but how would that work with `mod_increment`)? And is `np.vectorize` or
similar advisable to map `mod_increment` across array? (`profile` suggests
better as is though.)
"""
