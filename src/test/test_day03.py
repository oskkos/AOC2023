"""Advent of Code 2023 - Unit tests for day 3 tasks"""
from ..day03 import part_one
from .. import util


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
        ".664.598.."
    ]
    assert part_one(example_data) == 4361
    assert part_one(util.get_lines('day03')) == 540131
