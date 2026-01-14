"""
--- Day 4: Giant Squid ---
https://adventofcode.com/2021/day/4

TODO (possibly): might be an improvement to use sets and removal rather than
lists and '*'s (but good enough as is).
"""

from itertools import chain
from aocd import data

WINNING_LINE = ['*'] * 5


def parse(data):
    draws_chunk, *cards_chunk = data.split('\n\n')
    draws = [int(n) for n in draws_chunk.split(',')]
    cards = [
        [[int(n) for n in line.split()] for line in card.splitlines()]
        for card in cards_chunk
    ]
    return draws, cards


def count(card):
    # count all remaining numbers on a given card
    return sum([i for i in chain(*card) if isinstance(i, int)])


def wins(card):
    # return True if line of 5 '*'s found, False if not
    rows_and_cols = card + [list(col) for col in zip(*card)]
    return any(line == WINNING_LINE for line in rows_and_cols)


def mark_draw(n, cards):
    # given a number, cross it off all cards
    return [
        [['*' if i == n else i for i in row] for row in card]
        for card in cards
    ]


def play(draws, cards, target):
    # play game until target card found
    winners = set()
    for n in draws:
        cards = mark_draw(n, cards)
        for card_number, card in enumerate(cards):
            if card_number not in winners and wins(card):
                winners.add(card_number)
            if len(winners) == target:
                return count(card) * n


def part1(draws, cards):
    # find the first winning card
    return play(draws, cards, 1)


def part2(draws, cards):
    # find the last winning card
    return play(draws, cards, len(cards))


if __name__ == '__main__':
    draws, cards = parse(data)
    print('Part 1:', part1(draws, cards))
    print('Part 2:', part2(draws, cards))
