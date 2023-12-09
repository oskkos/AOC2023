"""Advent of Code 2023 - Unit tests for day 3 tasks"""
from .. import util
from ..day03 import part_one, part_two


def test_part_one():
    """
    Test function for part one of the AOC2023 day03 puzzle.

    This function tests the `part_one` function using example data and the actual puzzle input.
    It asserts that the output of `part_one` matches the expected values.

    Returns:
        None
    """
    example_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert part_one(example_data) == 4361
    assert part_one(util.get_lines("day03")) == 540131


def test_part_two():
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output
    for different input scenarios.

    Inputs:
    - example_data: A list of strings representing the example data.
    - util.get_lines('day03'): A list of strings representing the input data from 'day03' file.

    Returns:
    - None
    """
    example_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    assert part_two(example_data) == 467835
    assert part_two(["10*20"]) == 200
    assert part_two(util.get_lines("day03")) == 86879020
