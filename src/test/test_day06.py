"""Advent of Code 2023 - Unit tests for day 6 tasks"""
from ..day06 import part_one, part_two
from .. import util


def test_part_one():
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    example_data = [
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ]
    assert part_one(example_data) == 288
    assert part_one(util.get_lines('day06')) == 4403592


def test_part_two():
    """
    Test function for the part_two() function.

    This function tests the part_two() function using example data and the actual input data.
    It asserts that the output of part_two() matches the expected values.

    Returns:
        None
    """
    example_data = [
        "Time:      7  15   30",
        "Distance:  9  40  200"
    ]
    assert part_two(example_data) == 71503
    assert part_two(util.get_lines('day06')) == 38017587
