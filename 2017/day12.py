"""
--- Day 12: Digital Plumber ---
https://adventofcode.com/2017/day/12
"""

import re
from aocd import data


def parse(data):
    graph = {}
    for line in data.splitlines():
        node, *neighbors = re.findall(r'\d+', line)
        graph[node] = neighbors
    return graph


def part1(graph, node):
    return len(dfs(graph, node))


def part2(graph):
    nodes = set(graph.keys())
    i = 0
    while nodes:
        nodes -= dfs(graph, nodes.pop())
        i += 1
    return i


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

    return visited


if __name__ == '__main__':
    graph = parse(data)
    print('Part 1:', part1(graph, '0'))
    print('Part 2:', part2(graph))
