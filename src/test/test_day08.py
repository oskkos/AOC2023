"""Advent of Code 2023 - Unit tests for day 8 tasks"""
from ..day08 import part_one
from .. import util


def test_part_one():
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    example_data_1 = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)"
    ]
    example_data_2 = [
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)"
    ]
    assert part_one(example_data_1) == 2
    assert part_one(example_data_2) == 6
    assert part_one(util.get_lines('day08')) == 14257
