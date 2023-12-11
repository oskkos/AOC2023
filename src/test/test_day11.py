"""Advent of Code 2023 - Unit tests for day 11 tasks"""
from .. import util
from ..day11 import part_one

example_data: list[
    str
] = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split(
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

    assert part_one(example_data) == 374
    assert part_one(util.get_lines("day11")) == 10276166
