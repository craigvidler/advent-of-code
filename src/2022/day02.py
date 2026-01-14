"""
--- Day 2: Rock Paper Scissors ---
https://adventofcode.com/2022/day/2
"""

from aocd import data


BEATS = {'A': 'C', 'B': 'A', 'C': 'B'}
BASE_VALUE = {'A': 1, 'B': 2, 'C': 3}
WIN, DRAW, LOSE = 6, 3, 0
PART1_STRATEGY = {'X': 'A', 'Y': 'B', 'Z': 'C'}
PART2_STRATEGY = {
    'AX': 'C', 'AY': 'A', 'AZ': 'B',
    'BX': 'A', 'BY': 'B', 'BZ': 'C',
    'CX': 'B', 'CY': 'C', 'CZ': 'A'
}


def score(player1, player2):
    return BASE_VALUE[player2] + play(player1, player2)


def play(player1, player2):
    return (WIN if BEATS[player2] == player1
            else LOSE if BEATS[player1] == player2
            else DRAW)


def parse(data):
    return [line.split() for line in data.splitlines()]


def part1(games):
    return sum(
        score(player1, PART1_STRATEGY[player2])
        for player1, player2 in games
    )


def part2(games):
    return sum(
        score(player1, PART2_STRATEGY[player1 + player2])
        for player1, player2 in games
    )


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
