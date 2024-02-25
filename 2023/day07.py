"""
--- Day 7: Camel Cards ---
https://adventofcode.com/2023/day/7
"""

from collections import Counter
from aocd import data

# ie [High card, 1P, 2P, 3oaK, FH, 4oaK, 5oaK]
HANDS = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]
HAND_SCORES = {hand: score for score, hand in enumerate(HANDS)}
P1_CARD_ORDER = '23456789TJQKA'
P2_CARD_ORDER = 'J23456789TQKA'


def parse(data):
    return [line.split() for line in data.splitlines()]


def play(hands, card_order, wildcard=None):
    card_scores = {card: score for score, card in enumerate(card_order, 1)}
    if wildcard:
        wildcard = card_scores[wildcard]

    scored_cards = [score_cards(hand, card_scores) for hand in hands]
    sorted_hands = sorted(scored_cards, key=lambda hand: score_hand(hand, wildcard))

    return sum(bid * i for i, (score, bid) in enumerate(sorted_hands, 1))


def score_cards(hand, card_scores):
    cards, bid = hand
    return tuple(card_scores[card] for card in cards), int(bid)


def score_hand(hand, wildcard):
    cards, _ = hand
    c = Counter(cards)
    pattern = sorted(c.values())
    if wildcard and 0 < c[wildcard] < 5:
        pattern.remove(c[wildcard])
        pattern[-1] += c[wildcard]

    return HAND_SCORES[tuple(pattern)], cards


if __name__ == '__main__':
    hands = parse(data)
    print('Part 1:', play(hands, P1_CARD_ORDER))
    print('Part 2:', play(hands, P2_CARD_ORDER, wildcard='J'))
