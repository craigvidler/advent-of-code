"""
--- Day 12: Garden Groups ---
https://adventofcode.com/2024/day/12
"""

from aocd import data


def parse(data):
    return [list(line) for line in data.splitlines()]


def part1(grid):
    total = 0
    visited = set()
    islands = []

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if (r, c) not in visited:
                island = dfs(grid, r, c)
                islands.append(island)
                visited |= set(island)

    for island in islands:
        area = len(island)
        perimeter = 0

        for r, c in island:
            sided = 4
            for n in neighbors(r, c):
                if n in island:
                    sided -= 1

            perimeter += sided
        total += perimeter * area

    return total


def dfs(grid, r, c, visited=None):
    if visited is None:
        visited = set()

    if (r, c) not in visited:
        visited.add((r, c))
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == grid[r][c]:
                dfs(grid, nr, nc, visited)

    return visited


def neighbors(r, c):
    for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= nr < MAXROW and 0 <= nc < MAXCOL:
            yield nr, nc


if __name__ == "__main__":
    grid = parse(data)
    # For now. Don't like it but don't like alternatives either.
    MAXROW, MAXCOL = len(grid), len(grid[0])
    print("Part 1:", part1(grid))
