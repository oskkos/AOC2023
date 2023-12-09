"""Advent of Code 2023 - Day 3 tasks"""

import re
from curses.ascii import isdigit

# pylint: disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    --- Day 3: Gear Ratios ---
        You and the Elf eventually reach a gondola lift station; he says the gondola lift will take
        you up to the water source, but this is as far as he can bring you. You go inside.

        It doesn't take long to find the gondolas, but there seems to be a problem:
        they're not moving.

        "Aaah!"

        You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry,
        I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while
        before I can fix it." You offer to help.

        The engineer explains that an engine part seems to be missing from the engine,
        but nobody can figure out which one. If you can add up all the part numbers in the engine
        schematic, it should be easy to work out which part is missing.

        The engine schematic (your puzzle input) consists of a visual representation of the engine.
        There are lots of numbers and symbols you don't really understand, but apparently any
        number adjacent to a symbol, even diagonally, is a "part number" and should be
        included in your sum.
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
        In this schematic, two numbers are not part numbers because they are not adjacent
        to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent
        to a symbol and so is a part number; their sum is 4361.

        Of course, the actual engine schematic is much larger. What is the sum of all of the part
        numbers in the engine schematic?
    """
    total = 0
    for i, line in enumerate(lines):
        numbers = re.findall(r"\d+", line)
        if not numbers:
            continue
        j = 0
        for number in numbers:
            j = line.find(number, j)
            if check_if_number_is_adjacent_to_symbol(i, j, lines, number):
                total += int(number)
    return total


def part_two(lines: list[str]) -> int:
    """
    --- Part Two ---
    The engineer finds the missing part and installs it in the engine! As the engine springs to
    life, you jump in the closest gondola, finally ready to ascend to the water source.

    You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately,
    the gondola has a phone labeled "help", so you pick it up and the engineer answers.

    Before you can explain the situation, she suggests that you look out the window. There
    stands the engineer, holding a phone in one hand and waving with the other. You're going
    so slowly that you haven't even left the station. You exit the gondola.

    The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is
    any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of
    multiplying those two numbers together.

    This time, you need to find the gear ratio of every gear and add them all up so that the
    engineer can figure out which gear needs to be replaced.

    Consider the same engine schematic again:

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
    In this schematic, there are two gears. The first is in the top left; it has part numbers
    467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear
    ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one
    part number.) Adding up all of the gear ratios produces 467835.

    What is the sum of all of the gear ratios in your engine schematic?
    """
    total = 0
    for i, row in enumerate(lines):
        for j, cell in enumerate(row):
            if cell == "*":
                adjacent_nums: list[int] = get_adjacent_numbers(i, j, lines)
                if len(adjacent_nums) == 2:
                    total += int(adjacent_nums[0]) * int(adjacent_nums[1])
    return total


def check_if_number_is_adjacent_to_symbol(
    i: int, j: int, lines: list[str], number: str
) -> bool:
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
    for ii in range(i - 1, i + 2):
        if out_of_bounds(ii, lines):
            continue
        for jj in range(j - 1, j + len(number) + 1):
            if out_of_bounds(jj, lines[ii]):
                continue
            if re.search(r"[^\d.]", lines[ii][jj].strip()):
                return True
    return False


def get_adjacent_numbers(i: int, j: int, lines: list[str]) -> list[int]:
    """
    Get the adjacent numbers around a given position in a 2D grid.

    Args:
        i (int): The row index of the position.
        j (int): The column index of the position.
        lines (List[str]): The 2D grid represented as a list of strings.

    Returns:
        List[int]: A list of adjacent numbers.
    """
    adjacent: list[int] = []
    for ii in range(i - 1, i + 2):
        if out_of_bounds(ii, lines):
            continue
        last_seen_col = -1
        for jj in range(j - 1, j + 2):
            if out_of_bounds(jj, lines[ii]):
                continue
            if jj < last_seen_col:
                continue
            if isdigit(lines[ii][jj]):
                num, last_seen_col = resolve_whole_num(jj, lines[ii])
                adjacent.append(num)
    return adjacent


def out_of_bounds(index: int, items: str | list[str]) -> bool:
    """
    Check if the given index is out of bounds for the given list of items.

    Args:
        index (int): The index to check.
        items (list): The list of items.

    Returns:
        bool: True if the index is out of bounds, False otherwise.
    """
    return index < 0 or index >= len(items)


def resolve_whole_num(i: int, line: str) -> tuple[int, int]:
    """
    Resolves a whole number from a given position in a line.

    Args:
        i (int): The index of the character in the line.
        line (str): The line of characters.

    Returns:
        tuple: A tuple containing the resolved whole number and the index of the last
               character in the number.
    """
    num = line[i]
    reverse = i - 1
    while reverse >= 0 and isdigit(line[reverse]):
        num = line[reverse] + num
        reverse -= 1

    forward = i + 1
    while forward < len(line) and isdigit(line[forward]):
        num += line[forward]
        forward += 1

    return int(num), forward


if __name__ == "__main__":
    file_lines = util.get_lines("day03")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
