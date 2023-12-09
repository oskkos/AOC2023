"""Advent of Code 2023 - Unit tests for day 5 tasks"""
from .. import util
from ..day05 import part_one, part_two

example_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".split(
    "\n"
)
print(example_data)


def test_part_one():
    """
    Test function for part_one.

    This function tests the implementation of the part_one function by providing example
    data and asserting the expected output.

    Returns:
        None
    """

    assert part_one(example_data) == 35
    assert part_one(util.get_lines("day05")) == 265018614


def test_part_two():
    """
    Test function for the part_two() function.

    This function tests the part_two() function using example data and the actual input data.
    It asserts that the output of part_two() matches the expected values.

    Returns:
        None
    """

    assert part_two(example_data) == 46
    # assert part_two(util.get_lines('day05')) == 63179500
