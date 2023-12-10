"""Advent of Code 2023 - Unit tests for day 10 tasks"""
from .. import util
from ..day10 import part_one, part_two


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    example_data_1 = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ]
    example_data_2 = [
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    ]
    assert part_one(example_data_1) == 4
    assert part_one(example_data_2) == 8
    assert part_one(util.get_lines("day10")) == 6613


def test_part_two() -> None:
    """
    Test case for the part_two function.

    This test case asserts that the output of the part_two function, when called with the input from "day10" file,
    is equal to 511.
    """
    assert part_two(util.get_lines("day10")) == 511
