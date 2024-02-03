"""
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""

import re
from aocd import data


def parse(data):
    cards = []
    for line in data.splitlines():
        _, winners, haves = re.split(r'\||:', line)
        cards.append((
            set(winners.split()),
            set(haves.split())
        ))
    return cards


def part1(cards):
    return sum(2 ** (score - 1) for score in score_cards(cards) if score > 0)


def part2(cards):
    scores = score_cards(cards)
    counts = [1] * len(scores)

    for i, score in enumerate(scores):
        for j in range(i + 1, i + 1 + score):
            counts[j] += counts[i]

    return sum(counts)


def score_cards(cards):
    return [len(winners & haves) for winners, haves in cards]


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
