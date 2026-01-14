"""
--- Day 1: The Tyranny of the Rocket Equation ---
https://adventofcode.com/2019/day/1
"""

from aocd import data


def calc_fuel(mass, recursive=False):
    fuel = mass // 3 - 2
    if not recursive:
        return fuel
    return 0 if fuel <= 0 else fuel + calc_fuel(fuel, recursive=True)


def part1(modules):
    return sum(calc_fuel(module) for module in modules)


def part2(modules):
    return sum(calc_fuel(module, recursive=True) for module in modules)


if __name__ == '__main__':
    parsed = [int(line) for line in data.splitlines()]
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
