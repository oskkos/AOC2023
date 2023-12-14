"""Advent of Code 2023 - Unit tests for day 12 tasks"""
from .. import util
from ..day12 import part_one, part_two

example_data: list[
    str
] = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split(
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
    assert part_one(example_data) == 21
    assert part_one(util.get_lines("day12")) == 8270


def test_part_two() -> None:
    """
    Test function for part_two.

    This function tests the implementation of the part_two function by providing example
    data and asserting the expected output.

    Returns:
        None
    """

    assert part_two(example_data) == 525152
    assert part_two(util.get_lines("day12")) == 204640299929836
