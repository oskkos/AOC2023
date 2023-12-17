"""Advent of Code 2023 - Unit tests for day 16 tasks"""
from .. import util
from ..day16 import part_one, part_two

example_data: list[
    str
] = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....""".split(
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
    assert part_one(example_data) == 46
    assert part_one(util.get_lines("day16")) == 6605


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by providing example
    data and asserting the expected output.

    Returns:
        None
    """
    assert part_two(example_data) == 51
    # assert part_two(util.get_lines("day16")) == 6766 # takes a couple of minutes :-/
