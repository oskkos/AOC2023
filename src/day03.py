"""Advent of Code 2023 - Day 3 tasks"""

import re

# pylint: disable=import-error
if __package__ is None or __package__ == '':
    import util
else:
    from . import util


def part_one(lines):
    """
--- Day 3: Gear Ratios ---
    You and the Elf eventually reach a gondola lift station; he says the gondola lift will take
    you up to the water source, but this is as far as he can bring you. You go inside.

    It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

    "Aaah!"

    You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry,
    I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while
    before I can fix it." You offer to help.

    The engineer explains that an engine part seems to be missing from the engine, but nobody can
    figure out which one. If you can add up all the part numbers in the engine schematic, it should
    be easy to work out which part is missing.

    The engine schematic (your puzzle input) consists of a visual representation of the engine.
    There are lots of numbers and symbols you don't really understand, but apparently any number
    adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum.
    (Periods (.) do not count as a symbol.)

    Here is an example engine schematic:

    467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
    114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is
    a part number; their sum is 4361.

    Of course, the actual engine schematic is much larger. What is the sum of all of the part
    numbers in the engine schematic?
    """
    total = 0
    for i, line in enumerate(lines):
        numbers = re.findall(r'\d+', line)
        if not numbers:
            continue
        j = 0
        for number in numbers:
            j = line.find(number, j)
            if check_if_number_is_adjacent_to_symbol(i, j, lines, number):
                total += int(number)
    return total


def check_if_number_is_adjacent_to_symbol(i, j, lines, number):
    """
    Checks if a number is adjacent to a symbol in the given lines of text.

    Args:
        i (int): The row index of the number.
        j (int): The column index of the number.
        lines (list): The lines of text.
        number (str): The number to check.

    Returns:
        bool: True if the number is adjacent to a symbol, False otherwise.
    """
    for ii in range(i-1, i+2):
        if ii < 0 or ii >= len(lines):
            continue
        for jj in range(j-1, j+len(number)+1):
            if jj < 0 or jj >= len(lines[ii]):
                continue
            if re.search(r'[^\d.]', lines[ii][jj].strip()):
                print(lines[ii][jj], number)
                return True
    return False


file_lines = util.get_lines('day03')
print("Part one: " + str(part_one(file_lines)))
