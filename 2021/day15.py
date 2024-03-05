"""
--- Day 15: Chiton ---
https://adventofcode.com/2021/day/15

Version 1: runs slow (~3.75s, 2014 MacBook Air), due to inefficiently building a
big adjacency list in part 2, according to `profile`.
"""

from heapq import heappop, heappush
from aocd import data
import numpy as np

START = (0, 0)


def parse(data):
    return [[int(n) for n in line] for line in data.splitlines()]


def make_p2_map(p1_map, repeat):
    increment = np.vectorize(lambda n, i: (n + i - 1) % 9 + 1)
    tile = np.array(p1_map)
    col = np.vstack([increment(tile.copy(), i) for i in range(repeat)])
    return np.hstack([increment(col.copy(), i) for i in range(repeat)])


def make_graph(risk_map):
    maxrow, maxcol = len(risk_map) - 1, len(risk_map[0]) - 1
    return {
        (r, c): get_neighbors(r, c, risk_map, maxrow, maxcol)
        for r, row in enumerate(risk_map)
        for c, n in enumerate(row)
    }, (maxrow, maxcol)


def get_neighbors(r, c, risk_map, maxrow, maxcol):
    neighbors = []
    for nrow, ncol in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= nrow <= maxrow and 0 <= ncol <= maxcol:
            neighbors.append((risk_map[nrow][ncol], (nrow, ncol)))
    return neighbors


def dijkstra(graph, end):
    pq = [(0, START)]
    visited = set()

    while pq:
        cost, current = heappop(pq)
        if current == end:
            return cost
        for n_cost, neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                heappush(pq, (cost + n_cost, neighbor))


def solve(risk_map):
    graph, end = make_graph(risk_map)
    total = dijkstra(graph, end)
    return total


if __name__ == '__main__':
    p1_map = parse(data)
    p2_map = make_p2_map(p1_map, repeat=5)
    print('Part 1:', solve(p1_map))
    print('Part 2:', solve(p2_map))
