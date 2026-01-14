"""
--- Day 12: Hill Climbing Algorithm ---
https://adventofcode.com/2022/day/12

TODO/COULDDO: Probably an improvement (leaner code and faster execution) to
switch from using a pre-calculated adjacency list to dynamically finding
neighbors on the fly (see 2021, Day 15).
"""

from collections import defaultdict, deque
from aocd import data

def parse(data):
    """
    Map the row/col of each location in grid to its letter, eg {(0, 0): 'a'}.
    """
    mapping = {}
    for r, row in enumerate(data.splitlines()):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
                char = 'a'
            if char == 'E':
                end = (r, c)
                char = 'z'
            mapping[(r, c)] = char
    return mapping, start, end


def make_graph(mapping, can_step):
    """
    Create adjacency list following the height/step rule given for p1; for p2,
    reverse the rule to allow the same or similar path in reverse. Eg in
    p1 'm' can step to 'a' - 'n'; in p2, 'm' can step to 'l' - 'z'.
    """
    graph = defaultdict(list)
    for (r, c), level in mapping.items():
        for neighbor in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            # exclude out-of-bounds co-ords then test each part's `can_step`
            if neighbor_level := mapping.get(neighbor, None):
                if can_step(level, neighbor_level):
                    graph[(r, c)].append(neighbor)
    return graph


def bfs(graph, start, stop_when):
    """Return shortest path as list, both ends inclusive."""
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        visited.add(current)
        if stop_when(current):  # test stop condition
            return path + [current]
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current]))


def solve(mapping, start_at, can_step, stop_when):
    graph = make_graph(mapping, can_step)
    path = bfs(graph, start_at, stop_when)
    return len(path) - 1   # total edges in path


if __name__ == '__main__':
    mapping, start, end = parse(data)

    # p1: start at 'S', stop at 'E'; p2: start at 'E', stop at first 'a'
    p1_params = {
        'start_at': start,
        'can_step': lambda a, b: ord(a) >= ord(b) - 1,
        'stop_when': lambda current: current == end
    }
    p2_params = {
        'start_at': end,
        'can_step': lambda a, b: ord(b) >= ord(a) - 1,
        'stop_when': lambda current: mapping[current] == 'a'
    }

    print('Part 1:', solve(mapping, **p1_params))
    print('Part 2:', solve(mapping, **p2_params))
