"""Advent of Code 2023 - Day 13 tasks"""


# pylint:disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    Calculate the total score for a given list of patterns.

    Args:
        lines (list[str]): The list of patterns.

    Returns:
        int: The total score.
    """
    total = 0
    patterns = lines_to_patterns(lines)
    for pattern in patterns:
        h_score = calc_horizontal_score(pattern)
        if h_score:
            total += 100 * h_score

        v_score = calc_vertical_score(pattern)
        if v_score:
            total += v_score

    return total


def part_two(lines: list[str]) -> int:
    """
    Calculates the total score for a given list of patterns.

    Args:
        lines (list[str]): The list of patterns.

    Returns:
        int: The total score.
    """
    total = 0
    patterns = lines_to_patterns(lines)
    for pattern in patterns:
        for i in range(len(pattern) - 1):
            h_score = check_horizontal_match2(pattern, i)
            if h_score:
                total += 100 * h_score

        for col in range(len(pattern[0]) - 1):
            v_col = check_vertical_match2(pattern, col)
            if v_col:
                total += v_col

    return total


def lines_to_patterns(lines: list[str]) -> list[list[str]]:
    """
    Converts a list of lines into a list of patterns.

    Args:
        lines (list[str]): The input lines to be converted into patterns.

    Returns:
        list[list[str]]: A list of patterns, where each pattern is a list of strings.
    """
    patterns: list[list[str]] = []
    pattern: list[str] = []
    for line in lines:
        if not line:
            patterns.append(pattern)
            pattern = []
            continue
        pattern.append(line)
    patterns.append(pattern)
    return patterns


def calc_vertical_score(pattern: list[str]) -> int:
    """
    Calculate the vertical score of a pattern.

    Args:
        pattern (list[str]): The pattern to calculate the vertical score for.

    Returns:
        int: The vertical score of the pattern.
    """
    row_len = len(pattern[0])
    for i in range(row_len - 1):
        all_match = True
        for line in pattern:
            if line[i] != line[i + 1]:
                all_match = False
                break
        if all_match and check_vertical_match(pattern, i):
            return i + 1
    return 0


def check_vertical_match(pattern: list[str], col_nbr: int) -> bool:
    """
    Check if there is a vertical match in the given pattern at the specified column number.

    Args:
        pattern (list[str]): The pattern to check for a vertical match.
        col_nbr (int): The column number to check.

    Returns:
        bool: True if there is a vertical match, False otherwise.
    """
    for line in pattern:
        a = col_nbr
        b = col_nbr + 1
        while True:
            if line[a] != line[b]:
                return False
            a -= 1
            b += 1
            if a < 0 or b >= len(pattern[0]):
                break
    return True


def check_vertical_match2(pattern: list[str], col_nbr: int) -> int:
    """
    Check if there is a vertical match in the given pattern at the specified column number.

    Args:
        pattern (list[str]): The pattern to check for vertical match.
        col_nbr (int): The column number to check.

    Returns:
        int: The column number if there is a vertical match, otherwise 0.
    """
    smudges = 0
    for line in pattern:
        a = col_nbr
        b = col_nbr + 1
        while True:
            if line[a] != line[b]:
                smudges += 1
                if smudges > 1:
                    return 0
            a -= 1
            b += 1
            if a < 0 or b >= len(pattern[0]):
                break
    if not smudges:
        return 0
    return col_nbr + 1


def calc_horizontal_score(pattern: list[str]) -> int:
    """
    Calculates the horizontal score of a pattern.

    Args:
        pattern (list[str]): The pattern to calculate the score for.

    Returns:
        int: The horizontal score of the pattern.
    """
    for i, line in enumerate(pattern):
        if i + 1 == len(pattern):
            break
        if line == pattern[i + 1] and check_horizontal_match(pattern, i):
            return i + 1
    return 0


def check_horizontal_match(pattern: list[str], row_nbr: int) -> bool:
    """
    Check if there is a horizontal match in the pattern starting from the given row number.

    Args:
        pattern (list[str]): The pattern to check for a horizontal match.
        row_nbr (int): The starting row number.

    Returns:
        bool: True if there is a horizontal match, False otherwise.
    """
    a = row_nbr
    b = row_nbr + 1
    while True:
        if pattern[a] != pattern[b]:
            return False
        a -= 1
        b += 1
        if a < 0 or b >= len(pattern):
            break
    return True


def check_horizontal_match2(pattern: list[str], row_nbr: int) -> int:
    """
    Check for a horizontal match between two rows in a pattern.

    Args:
        pattern (list[str]): The pattern to check.
        row_nbr (int): The row number to start the check from.

    Returns:
        int: The row number if a horizontal match is found, otherwise 0.
    """
    smudges = 0
    a = row_nbr
    b = row_nbr + 1
    while True:
        if a < 0 or b >= len(pattern):
            break
        for i in range(len(pattern[a])):
            if pattern[a][i] != pattern[b][i]:
                smudges += 1
                if smudges > 1:
                    return 0
        a -= 1
        b += 1
    if not smudges:
        return 0
    return row_nbr + 1


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day13"))))
    print("Part two: " + str(part_two(util.get_lines("day13"))))
