"""
--- Day 5: Binary Boarding ---
https://adventofcode.com/2020/day/5#part2
"""


from aocd import data

TRANS = str.maketrans('FBLR', '0101')


def parse(data):
    # eg 'BBFFFBFRLL' -> '1100010100' -> decimal<1100010> * 8 + decimal<100> -> 788
    return [
        (int(line[:7], 2) * 8 + int(line[7:], 2))
        for line in data.translate(TRANS).splitlines()
    ]


def part1(seat_ids):
    return max(seat_ids)


def part2(seat_ids):
    # find the missing one
    [my_seat] = set(range(min(seat_ids), max(seat_ids) + 1)) - set(seat_ids)
    return my_seat


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
