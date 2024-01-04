"""
--- Day 4: Passport Processing ---
https://adventofcode.com/2020/day/4
"""

import re
from aocd import data


def parse(data):
    return [
        prep(dict(field.split(':') for field in passport.split()))
        for passport in data.split('\n\n')
    ]


def prep(pp):
    out = {}
    for k, v in pp.items():
        out[k] = v
        if k.endswith('yr'):  # convert years to ints
            out[k] = int(v)
        if k == 'hgt':  # process height
            out[k] = parse_hgt(v)
    return out


def parse_hgt(hgt):
    # if hgt field is well-formed, return it in unitless cms, or 0
    if m := re.match(r'(\d+)(cm|in)', hgt):
        height = int(m.group(1))
        return height if m.group(2) == 'cm' else round(height * 2.54)
    return 0


def p1_valid(pp):
    return len(pp) == 8 or len(pp) == 7 and 'cid' not in pp


def p2_valid(pp):
    # ensure defaults for missing data
    return all((
        1920 <= pp.get('byr', 0) <= 2002,
        2010 <= pp.get('iyr', 0) <= 2020,
        2020 <= pp.get('eyr', 0) <= 2030,
        150 <= pp.get('hgt', 0) <= 193,
        re.fullmatch(r'#[0-9a-f]{6}', pp.get('hcl', '')),
        pp.get('ecl', '') in 'amb blu brn gry grn hzl oth'.split(),
        re.fullmatch(r'\d{9}', pp.get('pid', '')),
    ))


def part1(passports):
    return sum(p1_valid(pp) for pp in passports)


def part2(passports):
    return sum(p2_valid(pp) for pp in passports)


if __name__ == '__main__':
    parsed = parse(data)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
