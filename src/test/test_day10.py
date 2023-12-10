"""Advent of Code 2023 - Unit tests for day 10 tasks"""
from .. import util
from ..day10 import part_one


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
