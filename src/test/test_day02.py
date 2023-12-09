"""Advent of Code 2023 - Unit tests for day 2 tasks"""
from .. import util
from ..day02 import part_one, part_two


def test_part_one() -> None:
    """
    Test function for the part_one function.

    This function tests the part_one function using example data and the actual input data.
    It asserts that the output of the part_one function matches the expected values.

    Returns:
        None
    """
    example_data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert part_one(example_data) == 8
    assert part_one(util.get_lines("day02")) == 1867


def test_part_two() -> None:
    """
    Test function for the part_two function.

    This function tests the part_two function using example data and the actual input data.
    It asserts that the output of the part_two function matches the expected values.

    Returns:
        None
    """
    example_data = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    assert part_two(example_data) == 2286
    assert part_two(util.get_lines("day02")) == 84538
