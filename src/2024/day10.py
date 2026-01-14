"""
--- Day 10: Hoof It ---
https://adventofcode.com/2024/day/10
"""

from aocd import data


def parse(data):
    return [[int(c) for c in line] for line in data.splitlines()]


def neighbors(r, c):
    for nr, nc in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= nr < MAXROW and 0 <= nc < MAXCOL:
            yield nr, nc


def trailheads(grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == 0:
                yield r, c


def dfs(grid, r, c):
    if grid[r][c] == 9:
        return [(r, c)]  # using coords of each 9 as unique id

    peaks_reached = []
    for nr, nc in neighbors(r, c):
        if grid[nr][nc] == grid[r][c] + 1:
            peaks_reached.extend(dfs(grid, nr, nc))

    return peaks_reached


def walk(grid):
    distinct_peaks = total_paths = 0

    for r, c in trailheads(grid):
        peaks_reached = dfs(grid, r, c)
        distinct_peaks += len(set(peaks_reached))
        total_paths += len(peaks_reached)

    return distinct_peaks, total_paths


if __name__ == "__main__":
    grid = parse(data)
    # For now. Don't like it but don't like alternatives either.
    MAXROW, MAXCOL = len(grid), len(grid[0])
    score, rating = walk(grid)
    print("Part 1:", score)
    print("Part 2:", rating)
