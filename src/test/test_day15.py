"""Advent of Code 2023 - Unit tests for day 15 tasks"""
from .. import util
from ..day15 import part_one, part_two

example_data: list[
    str
] = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".split("\n")


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    assert part_one(example_data) == 1320
    assert part_one(util.get_lines("day15")) == 510388


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    assert part_two(example_data) == 145
    assert part_two(util.get_lines("day15")) == 291774
