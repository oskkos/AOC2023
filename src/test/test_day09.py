"""Advent of Code 2023 - Unit tests for day 9 tasks"""
from ..day09 import part_one, part_two
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
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45"
    ]
    assert part_one(example_data) == 114
    assert part_one(util.get_lines('day09')) == 1898776583

def test_part_two():
    """
    Test case for the part_two function.

    This test case checks if the part_two function returns the expected output
    for the given example data and the input from the 'day09' file.

    Returns:
        None
    """
    example_data = [
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45"
    ]
    assert part_two(example_data) == 2
    assert part_two(util.get_lines('day09')) == 1100
