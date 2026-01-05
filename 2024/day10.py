"""
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10
"""

from aocd import data


def neighbors(r, c, grid):
    for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= nr < MAXROW and 0 <= nc < MAXCOL:
            yield nr, nc


def get_heads(grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 0:
                yield r, c


def dfs(grid, r, c, peaks):
    if ((r, c)) in peaks:
        return

    if grid[r][c] == 9:
        peaks.add((r, c))

    for nr, nc in neighbors(r, c, grid):
        if grid[nr][nc] == grid[r][c] + 1:
            dfs(grid, nr, nc, peaks)

    return peaks


def p2_dfs(grid, r, c, count):
    if grid[r][c] == 9:
        count += 1

    for nr, nc in neighbors(r, c, grid):
        if grid[nr][nc] == grid[r][c] + 1:
            count = p2_dfs(grid, nr, nc, count)

    return count


def parse(data):
    return [[int(c) for c in line] for line in data.splitlines()]


def part1(grid):
    total = 0
    for r, c in get_heads(grid):
        peaks = set()
        total += len(dfs(grid, r, c, peaks))
    return total


def part2(grid):
    total = count = 0
    for r, c in get_heads(grid):
        total += p2_dfs(grid, r, c, count)
    return total


if __name__ == "__main__":
    grid = parse(data)
    MAXROW, MAXCOL = len(grid), len(grid[0])
    print("Part 1:", part1(grid))
    print("Part 2:", part2(grid))
