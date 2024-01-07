"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""

from collections import Counter
from aocd import data


def apply_bit_criteria(col, mode):
    """
    OGR mode: return the most common bit value in a column; in a tie, return
    '1'. CSR mode: return the least common bit value; in a tie, return '0'.
    (`mc[-1]` is used because a column may contain only '1's or only '0's.
    `mc[1]` and other methods assuming two values in the Counter were
    failing when it contained only one.)
    """
    preferred_bit = '1' if mode == 'ogr' else '0'
    mc = Counter(col).most_common()
    most_common_bit, mcb_count = mc[0]
    least_common_bit, lcb_count = mc[-1]
    if mcb_count == lcb_count:
        return preferred_bit
    return most_common_bit if preferred_bit == '1' else least_common_bit


def filter_lines(lines, mode):
    """
    Iterate through the columns, filtering list down to a single value based
    on the bit criteria for each mode.
    """
    for i, _ in enumerate(lines[0]):
        cols = list(zip(*lines))
        key_bit = apply_bit_criteria(cols[i], mode)
        lines = [line for line in lines if line[i] == key_bit]
        if len(lines) == 1:
            return lines[0]


def part1(lines):
    """find the most common bit in each column, and the least"""
    most_commons = [max(col, key=col.count) for col in zip(*lines)]
    least_commons = ['0' if n == '1' else '1' for n in most_commons]
    gamma = ''.join(most_commons)
    epsilon = ''.join(least_commons)
    return int(gamma, 2) * int(epsilon, 2)


def part2(lines):
    """filter lines based on the bit criteria for each rating (OGR/CSR)"""
    ogr = filter_lines(lines.copy(), mode='ogr')
    csr = filter_lines(lines, mode='csr')
    return int(ogr, 2) * int(csr, 2)


if __name__ == '__main__':
    parsed = data.splitlines()
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
