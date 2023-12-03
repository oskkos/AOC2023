"""Advent of Code 2023 - Day 1 tasks"""

import re

# pylint: disable=import-error
if __package__ is None or not __package__:
    import util
else:
    from . import util


def part_one(lines):
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
    for line in lines:
        numbers = get_first_and_last_number_digits_only(line)
        total += int(numbers)
    return total


def part_two(lines):
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
    for line in lines:
        numbers = get_first_and_last_number_digits_or_written(line)
        total = total + int(numbers)
    return total

def get_first_and_last_number_digits_only(line):
    """
    Extracts the first and last digits from a given line.

    Args:
        line (str): The input line containing digits.

    Returns:
        str: The first and last digits concatenated as a string.
    """
    digits = ''.join(re.findall("\\d+", line))
    return str(digits[0]) + str(digits[-1])


def get_first_and_last_number_digits_or_written(line):
    """
    Get the first and last occurrence of a number (digit or written) from a given line.

    Args:
        line (str): The input line.

    Returns:
        str: A string representing the concatenation of the indices of the
             first and last occurrences of number (digit or written).
    """
    substrings = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    min_index = len(line)
    max_index = -1
    first = ""
    last = ""
    for sub in substrings:
        a = line.find(sub)
        if (a != -1 and a < min_index):
            min_index = a
            first = sub
        b = line.rfind(sub)
        if (b != -1 and b > max_index):
            max_index = b
            last = sub
    first_num = first if first.isdigit() else str(substrings.index(first) + 1)
    last_num = last if last.isdigit() else str(substrings.index(last) + 1)
    return first_num + last_num


file_lines = util.get_lines('day01')
print("Part one: " + str(part_one(file_lines)))
print("Part two: " + str(part_two(file_lines)))
