"""Advent of Code 2023 - Unit tests for day 7 tasks"""
from .. import util
from ..day07 import part_one, part_two

example_data = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]


def test_part_one():
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    assert part_one(example_data) == 6440
    assert part_one(util.get_lines("day07")) == 249638405


def test_part_two():
    """
    Test function for the part_two() function.

    This function tests the part_two() function using example data and the actual input data.
    It asserts that the output of part_two() matches the expected values.

    Returns:
        None
    """
    assert part_two(example_data) == 5905
    assert part_two(util.get_lines("day07")) == 249776650
