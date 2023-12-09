"""Advent of Code 2023 - Unit tests for day 1 tasks"""
from .. import util
from ..day01 import part_one, part_two


def test_part_one():
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by asserting the expected output
    for both example data and the actual input data.

    Returns:
        None
    """
    example_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    assert part_one(example_data) == 142
    assert part_one(util.get_lines("day01")) == 55029


def test_part_two():
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by asserting the expected output
    for both example data and the data from the 'day01' file.

    Returns:
        None
    """
    example_data = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    assert part_two(example_data) == 281
    assert part_two(util.get_lines("day01")) == 55686
