"""Advent of Code 2023 - Day 8 tasks"""

import re
from math import lcm

# pylint: disable=import-error
if __package__ is None or not __package__:
    import util
else:
    from . import util


def part_one(lines):
    """
    Calculate the result of part one of the puzzle.

    Args:
        lines (list): List of input lines.

    Returns:
        int: The result of part one.
    """
    instructions, mapping = instructions_and_mapping(lines)
    return runner(instructions, mapping, "AAA", "ZZZ")


def part_two(lines):
    """
    Calculate the least common multiple (LCM) of the execution times of all nodes
    ending with 'A' in the given instructions.

    Args:
        lines (list): List of instructions.

    Returns:
        int: The least common multiple (LCM) of the execution times.
    """
    instructions, mapping = instructions_and_mapping(lines)
    filtered_mapping = {}
    for key, value in mapping.items():
        if key.endswith("A"):
            filtered_mapping[key] = value

    current = filtered_mapping.keys()

    lcms = [runner(instructions, mapping, node, "Z") for node in current]
    return lcm(*lcms)


def instructions_and_mapping(lines):
    """
    Extracts instructions and creates a mapping from the given lines.

    Args:
        lines (list[str]): A list of values in the format AAA (BBB,CCC).

    Returns:
        dict: A mapping of instructions.

    """
    instructions = lines.pop(0).strip()
    mapping = {}
    for line in lines:
        if not line.strip():
            continue
        chunks = re.findall(r"[\dA-Z]+", line)
        mapping[chunks.pop(0)] = chunks
    return instructions, mapping


def runner(instructions, mapping, current, ending):
    """
    Runs the instructions on the mapping to find the number of steps required to
    reach a sequence ending with the specified ending.

    Args:
        instructions (list): List of instructions.
        mapping (dict): Mapping of sequences.
        current (str): Current sequence.
        ending (str): Ending sequence.

    Returns:
        int: Number of steps required to reach the ending sequence.
    """
    steps = 0
    pos = 0
    while True:
        direction = instructions[pos]
        next_seq = mapping[current][0 if direction == "L" else 1]
        steps += 1

        if next_seq.endswith(ending):
            return steps

        current = next_seq
        pos += 1
        if pos == len(instructions):
            pos = 0


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day08"))))
    print("Part two: " + str(part_two(util.get_lines("day08"))))
