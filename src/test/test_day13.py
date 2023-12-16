"""Advent of Code 2023 - Unit tests for day 13 tasks"""
from .. import util
from ..day13 import part_one, part_two

example_data: list[
    str
] = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

.#.##.#.#
.##..##..
.#.##.#..
#......##
#......##
.#.##.#..
.##..##.#

#..#....#
###..##..
.##.#####
.##.#####
###..##..
#..#....#
#..##...#

#.##..##.
..#.##.#.
##..#...#
##...#..#
..#.##.#.
..##..##.
#.#.##.#.""".split(
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
    assert part_one(example_data) == 709
    assert part_one(util.get_lines("day13")) == 37561


def test_part_two() -> None:
    """
    Test case for the part_two function.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    assert part_two(example_data) == 1400
    assert part_two(util.get_lines("day13")) == 31108
