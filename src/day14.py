"""Advent of Code 2023 - Day 14 tasks"""


from functools import cache

# pylint:disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    Calculates the result for part one of the problem.

    Args:
        lines (list[str]): The input lines.

    Returns:
        int: The result for part one.
    """

    tilted = tilt_north("^".join(lines))
    return calculate_total(tilted.split("^"))


def part_two(lines: list[str]) -> int:
    """
    Calculates the result for part two of the problem.

    Args:
        lines (list[str]): The input lines.

    Returns:
        int: The result for part two.
    """
    for _ in range(1000000000):
        lines = cycle(lines)

    return calculate_total(lines)


def calculate_total(lines: list[str]) -> int:
    """
    Calculates the total based on the lines provided.

    Args:
        lines (list[str]): The list of lines to calculate the total from.

    Returns:
        int: The calculated total.

    """
    total = 0
    for i, line in enumerate(lines):
        for char in line:
            if char == "O":
                total += len(line) - i

    return total


def cycle(lines: list[str]) -> list[str]:
    """
    Cycles the tiles in the grid.

    Args:
        lines (list[str]): The input lines.

    Returns:
        list[str]: The updated lines.
    """
    line_str = "^".join(lines)

    line_str = tilt_north(line_str)
    line_str = tilt_west(line_str)
    line_str = tilt_south(line_str)
    line_str = tilt_east(line_str)

    lines = line_str.split("^")
    return lines


@cache
def tilt_north(line_str: str) -> str:
    """
    Tilt the 'O's in given line string towards the north.

    Args:
        line_str (str): The input line string.

    Returns:
        str: The tilted line string.

    """
    lines = line_str.split("^")

    ret = []
    for line in lines:
        ret.append(line.replace("O", "."))

    next_avail = {}
    for j in range(len(lines[0])):
        next_avail[j] = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "O":
                if next_avail[j] < len(lines):
                    ret[next_avail[j]] = replace_char_at_index(
                        ret[next_avail[j]], j, "O"
                    )
                next_avail[j] += 1
            elif char == "#":
                next_avail[j] = i + 1
    return "^".join(ret)


@cache
def tilt_south(line_str: str) -> str:
    """
    Tilt the 'O's in given line string towards the south.

    Args:
        line_str (str): The input line string.

    Returns:
        str: The tilted line string.

    """
    lines = line_str.split("^")

    ret = []
    for line in lines:
        ret.append(line.replace("O", "."))

    next_avail = {}
    for j in range(len(lines[0])):
        next_avail[j] = len(lines) - 1

    for i, line in enumerate(reversed(lines)):
        original_index = len(lines) - 1 - i
        for j, char in enumerate(line):
            if char == "O":
                if next_avail[j] < len(lines):
                    ret[next_avail[j]] = replace_char_at_index(
                        ret[next_avail[j]], j, "O"
                    )
                next_avail[j] -= 1
            elif char == "#":
                next_avail[j] = original_index - 1
    return "^".join(ret)


@cache
def tilt_west(line_str: str) -> str:
    """
    Tilt the 'O's in given line string towards the west.

    Args:
        line_str (str): The input line string.

    Returns:
        str: The tilted line string.
    """
    lines = line_str.split("^")
    return "^".join(list(map(line_to_west, lines)))


@cache
def tilt_east(line_str: str) -> str:
    """
    Tilt the 'O's in given line string towards the east.

    Args:
        line_str (str): The line string to be tilted.

    Returns:
        str: The tilted line string.
    """
    lines = line_str.split("^")
    return "^".join(list(map(line_to_east, lines)))


def line_to_west(line: str) -> str:
    """
    Converts a line of strings to a single string by joining them with '#'
    and sorting them in westward direction.

    Args:
        line (str): The line of strings to be converted.

    Returns:
        str: The converted string.
    """
    return "#".join(list(map(sort_string_west, line.split("#"))))


def sort_string_west(s: str) -> str:
    """
    Sorts the characters in a string in descending order.

    Args:
        s (str): The input string to be sorted.

    Returns:
        str: The sorted string in descending order.
    """
    return "".join(sorted(s, reverse=True))


def line_to_east(line: str) -> str:
    """
    Converts a line of strings to a single string by joining them with '#'
    and sorting them in ascending order.

    Args:
        line (str): The input line of strings.

    Returns:
        str: The converted string.
    """
    return "#".join(list(map(sort_string_east, line.split("#"))))


def sort_string_east(s: str) -> str:
    """
    Sorts the characters in a string in ascending order.

    Args:
        s (str): The input string to be sorted.

    Returns:
        str: The sorted string.

    """
    return "".join(sorted(s, reverse=False))


def replace_char_at_index(string: str, index: int, new_char: str) -> str:
    """
    Replaces a character at a specific index in a string with a new character.

    Args:
        string (str): The input string.
        index (int): The index of the character to be replaced.
        new_char (str): The new character to replace the existing character.

    Returns:
        str: The modified string with the character replaced.
    """
    string_list = list(string)
    string_list[index] = new_char
    return "".join(string_list)


def create_string_with_dots(x: int) -> str:
    """
    Creates a string with dots.

    Args:
        x (int): The number of dots to include in the string.

    Returns:
        str: A string consisting of 'x' number of dots.
    """
    return "." * x


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day14"))))
    # print("Part two: " + str(part_two(util.get_lines("day14")))) # too slow, took 3 hours :-/
