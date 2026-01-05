"""
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10
"""

from aocd import data


def neighbors(r, c, grid):
    for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= row < MAXROW and 0 <= col < MAXCOL:
            yield (row, col)


def get_heads(grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 0:
                yield r, c


def dfs(grid, r, c, level, visited=None):
    if visited is None:
        visited = set()

    if ((r, c), level) not in visited:
        visited.add(((r, c), level))
        for r, c in neighbors(r, c, grid):
            if grid[r][c] == level + 1:
                dfs(grid, r, c, level + 1, visited)

    return visited


def parse(data):
    return [[int(c) for c in line] for line in data.splitlines()]


def part1(grid):
    total = 0

    for r, c in get_heads(grid):
        tails = dfs(grid, r, c, level=0)
        total += len([t for t, level in tails if level == 9])
    return total


if __name__ == "__main__":
    grid = parse(data)
    MAXROW, MAXCOL = len(grid), len(grid[0])
    print("Part 1:", part1(grid))
