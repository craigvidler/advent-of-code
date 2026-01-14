"""
--- Day 5: A Maze of Twisty Trampolines, All Alike ---
https://adventofcode.com/2017/day/5
"""

from aocd import data


def solve(instructions, postjump_shift=1):
    pointer = offset = i = 0
    while True:
        try:
            offset = instructions[pointer]
        except IndexError:
            return(i)

        instructions[pointer] += postjump_shift if offset >= 3 else 1
        pointer += offset
        i += 1


if __name__ == '__main__':
    instructions = [int(n) for n in data.splitlines()]
    print('Part 1:', solve(instructions.copy()))
    print('Part 2:', solve(instructions, postjump_shift=-1))
