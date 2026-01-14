"""
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""

from math import prod
from collections import defaultdict
import re
from aocd import data


def parse(data_lines):
    # numbers: {(0, 0, 2): 467, …} (line, start index, end index): number
    # symbols: {(1, 3): '*', …} (line, index: symbol)
    numbers = {}
    symbols = {}

    # not so keen on the nested double regex loops, but it works
    for i, line in enumerate(data_lines):

        for match in re.finditer(r'\d+', line):  # numbers
            start, end = match.span()
            # -1 to convert span length to index of end digit
            numbers[(i, start, end - 1)] = int(match.group(0))

        for match in re.finditer(r'[^\.\d]+', line):  # symbols
            position, _ = match.span()
            symbols[(i, position)] = match.group(0)

    return numbers, symbols


def part1(symbol_mapping):
    # symbol_mapping lists all symbols and their neighboring numbers; sum them.
    return sum(
        sum(numbers) for _, numbers in symbol_mapping.items()
    )


def part2(symbol_mapping):
    # From symbol_mapping get all '*'s with exactly two adjacent numbers; multiply
    # each pair and sum all products.
    return sum(
        prod(numbers) for (_, symbol), numbers in symbol_mapping.items()
        if symbol == '*' and len(numbers) == 2
    )


def get_neighbors(number_location):
    row, start_index, end_index = number_location

    # ensure we stay in bounds
    start_row = max(row - 1, 0)
    end_row = min(row + 1, schematic_height)
    start_index = max(start_index - 1, 0)
    end_index = min(end_index + 1, schematic_width)

    neighbors = []
    for i in range(start_row, end_row + 1):
        for j in range(start_index, end_index + 1):
            neighbors.append((i, j))

    return neighbors


def map_symbols(numbers, symbols):
    # symbol_mapping: lists all symbols mapped to their neighboring numbers.
    # {((1, 3), '*'): [467, 35], …} (row, index of symbol, symbol,
    # neighboring numbers). (If any number had multiple adjacent symbols,
    # we'd need to record each number's position as well to avoid duplicate
    # counting. No number has more than one though.)
    symbol_mapping = defaultdict(list)
    for number_location, number in numbers.items():
        for location in get_neighbors(number_location):
            if symbol := symbols.get(location, None):
                symbol_mapping[(location, symbol)].append(number)
    return symbol_mapping


if __name__ == '__main__':
    data_lines = data.splitlines()
    schematic_height = len(data_lines)
    schematic_width = len(data_lines[0])

    numbers, symbols = parse(data_lines)
    symbol_mapping = map_symbols(numbers, symbols)

    print('Part 1:', part1(symbol_mapping))
    print('Part 2:', part2(symbol_mapping))
