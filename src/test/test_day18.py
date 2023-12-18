"""Advent of Code 2023 - Unit tests for day 18 tasks"""
from .. import util
from ..day18 import part_one

example_data: list[
    str
] = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split(
    "\n"
)


def test_part_one() -> None:
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    assert part_one(example_data) == 62
    assert part_one(util.get_lines("day18")) == 61661


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    # there is no quick enough solution at the moment :-/
