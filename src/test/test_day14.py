"""Advent of Code 2023 - Unit tests for day 14 tasks"""
from .. import util
from ..day14 import part_one

example_data: list[
    str
] = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split(
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
    assert part_one(example_data) == 136
    assert part_one(util.get_lines("day14")) == 106997
