"""Advent of Code 2023 - Day 8 tasks"""

import re

# pylint: disable=import-error
if __package__ is None or not __package__:
    import util
else:
    from . import util


def part_one(lines):
    """
    part one
    """
    instructions = lines.pop(0).strip()
    mapping = {}
    for line in lines:
        if not line.strip():
            continue
        chunks = re.findall(r'[A-Z]+', line)
        mapping[chunks.pop(0)] = chunks

    steps = 0
    current = 'AAA'
    pos = 0
    while True:
        direction = instructions[pos]
        next_seq = mapping[current][0 if direction == 'L' else 1]
        steps +=1

        if next_seq == 'ZZZ':
            return steps

        current = next_seq
        pos +=1
        if pos == len(instructions):
            pos = 0
    return -1


if __name__ == "__main__":
    file_lines = util.get_lines('day08')
    print("Part one: " + str(part_one(file_lines)))
