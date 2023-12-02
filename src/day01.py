"""Advent of Code 2023 - Day 1 tasks"""

import re
import util


def part_one():
    """
    --- Day 1: Trebuchet?! ---
    Something is wrong with global snow production, and you've been selected to take a look.
    The Elves have even given you a map; on it, they've used stars to mark the top fifty locations
    that are likely to be having problems.

    You've been doing this long enough to know that to restore snow operations, you need to check
    all fifty stars by December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day in the
    Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants
    one star. Good luck!

    You try to ask why they can't just use a weather machine ("not powerful enough") and where
    they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of
    questions") and hang on did you just say the sky ("of course, where do you think snow comes
    from") when you realize that the Elves are already loading you into a trebuchet ("please hold
    still, we need to strap you in").

    As they're making the final adjustments, they discover that their calibration document (your
    puzzle input) has been amended by a very young Elf who was apparently just excited to show off
    her art skills. Consequently, the Elves are having trouble reading the values on the document.

    The newly-improved calibration document consists of lines of text; each line originally
    contained a specific calibration value that the Elves now need to recover. On each line, the
    calibration value can be found by combining the first digit and the last digit (in that order)
    to form a single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet
    In this example, the calibration values of these four lines are 12, 38, 15, and 77.
    Adding these together produces 142.

    Consider your entire calibration document. What is the sum of all of the calibration values?
    """
    total = 0
    for line in util.get_lines('day01'):
        numbers = get_numbers(line)
        total += int(numbers[0] + numbers[-1])
    print("Part one: " + str(total))


def part_two():
    """
    --- Part Two ---
    Your calculation isn't quite right. It looks like some of the digits are actually spelled out
    with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid
    "digits".

    Equipped with this new information, you now need to find the real first and last digit on each
    line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen
    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these 
    together produces 281.

    What is the sum of all of the calibration values?
    """
    total = 0
    for line in util.get_lines('day01'):
        numbers = get_numbers(replace_first_and_last_written_numbers(line))
        total += int(numbers[0] + numbers[-1])
    print("Part two: " + str(total))


def replace_first_and_last_written_numbers(line):
    """
    Replaces written numbers in a given line with their corresponding numeric representation.

    Args:
        line (str): The input line containing written numbers.

    Returns:
        str: The line with written numbers replaced by their numeric representation.
    """
    substrings = ['one', 'two', 'three', 'four',
                  'five', 'six', 'seven', 'eight', 'nine']
    found_substring = [sub for sub in substrings if sub in line]
    if not found_substring:
        return line

    max_index = -1
    min_index = len(line)
    first = ""
    last = ""
    for substr in found_substring:
        if line.find(substr) < min_index:
            min_index = line.find(substr)
            first = substr
        if line.rfind(substr) > max_index:
            max_index = line.rfind(substr)
            last = substr
    return (line
            .replace(first, str(substrings.index(first)+1) + first, 1)
            .replace(last, last + str(substrings.index(last) + 1)))


def get_numbers(line):
    """
    Extracts all the numbers from a given string.

    Args:
        line (str): The input string.

    Returns:
        str: A string containing all the numbers found in the input string.
    """
    return ''.join(re.findall("\\d+", line))


part_one()
part_two()
