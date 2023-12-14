"""Advent of Code 2023 - Day 14 tasks"""


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
    columns = combine_column_data(lines)
    return tilt_north_and_count(columns)


def tilt_north_and_count(columns: list[str]) -> int:
    """
    Tilt the columns to the north and count the number of tiles.

    Args:
        columns (list[str]): A list of strings representing the columns.

    Returns:
        int: The total number of tiles after tilting the columns to the north.
    """
    total = 0
    for x in columns:
        avail_ix = 0
        x2 = create_string_with_dots(len(x))
        for i, char in enumerate(x):
            if char == "O":
                x2 = replace_char_at_index(x2, avail_ix, "O")
                avail_ix += 1
            if char == "#":
                x2 = replace_char_at_index(x2, i, "#")
                avail_ix = i + 1

        for i, char in enumerate(x2):
            if char == "O":
                total += len(x2) - i
    return total


def combine_column_data(lines: list[str]) -> list[str]:
    """
    Combine the data from each column of a 2D list into a list of strings.

    Args:
        lines (list[str]): A 2D list of strings representing the data.

    Returns:
        list[str]: A list of strings where each string contains the combined data from each column.
    """
    rows = len(lines)
    columns = len(lines[0])

    cols: dict[int, str] = {}
    for col_nbr in range(columns):
        for row_nbr in range(rows):
            cols[col_nbr] = cols.get(col_nbr, "") + lines[row_nbr][col_nbr]
    return list(cols.values())


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
