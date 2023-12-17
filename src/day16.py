"""Advent of Code 2023 - Day 16 tasks"""


# pylint:disable=import-error
import sys


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

    sys.setrecursionlimit(5000)

    init_direction = ""
    if lines[0][0] in (".", "-"):
        init_direction = "right"
    if lines[0][0] in ("\\", "|"):
        init_direction = "down"
    return calculate_path_length(lines, 0, 0, init_direction)


# pylint:disable-next=too-many-branches
def part_two(lines: list[str]) -> int:
    """
    Calculates the result for part two of the problem.

    Args:
        lines (list[str]): The input lines.

    Returns:
        int: The result for part two.
    """

    sys.setrecursionlimit(5000)

    values = []
    # top row
    for i, char in enumerate(lines[0]):
        if char in (".", "|"):
            values.append(calculate_path_length(lines, 0, i, "down"))
        if char in ("/"):
            values.append(calculate_path_length(lines, 0, i, "left"))
        if char in ("\\"):
            values.append(calculate_path_length(lines, 0, i, "right"))
        if char in ("-"):
            values.append(calculate_path_length(lines, 0, i, "left"))
            values.append(calculate_path_length(lines, 0, i, "right"))

    # bottom row
    bottom_row = len(lines) - 1
    for i, char in enumerate(lines[len(lines) - 1]):
        if char in (".", "|"):
            values.append(calculate_path_length(lines, bottom_row, i, "up"))
        if char in ("/"):
            values.append(calculate_path_length(lines, bottom_row, i, "right"))
        if char in ("\\"):
            values.append(calculate_path_length(lines, bottom_row, i, "left"))
        if char in ("-"):
            values.append(calculate_path_length(lines, bottom_row, i, "left"))
            values.append(calculate_path_length(lines, bottom_row, i, "right"))

    # first col
    for i, line in enumerate(lines):
        char = line[0]
        if char in (".", "-"):
            values.append(calculate_path_length(lines, i, 0, "right"))
        if char in ("/"):
            values.append(calculate_path_length(lines, i, 0, "up"))
        if char in ("\\"):
            values.append(calculate_path_length(lines, i, 0, "down"))
        if char in ("|"):
            values.append(calculate_path_length(lines, i, 0, "up"))
            values.append(calculate_path_length(lines, i, 0, "down"))

    # last col
    last_col = len(lines[0]) - 1
    for i, line in enumerate(lines):
        char = line[last_col]
        if char in (".", "-"):
            values.append(calculate_path_length(lines, i, last_col, "left"))
        if char in ("/"):
            values.append(calculate_path_length(lines, i, last_col, "down"))
        if char in ("\\"):
            values.append(calculate_path_length(lines, i, last_col, "up"))
        if char in ("|"):
            values.append(calculate_path_length(lines, i, last_col, "up"))
            values.append(calculate_path_length(lines, i, last_col, "down"))

    return max(values)


def calculate_path_length(lines: list[str], i: int, j: int, direction: str) -> int:
    """
    Calculates the length of the path starting from the given position and direction.

    Args:
        lines (list[str]): The lines representing the path.
        i (int): The starting row index.
        j (int): The starting column index.
        direction (str): The starting direction.

    Returns:
        int: The length of the path.
    """
    seen: list[tuple[int, int, str]] = [(i, j, direction)]
    move(lines, seen, (i, j), direction)
    path_len = len(calc_seen(seen))
    print(f"{i}/{j} -> {direction}: {path_len}")
    return path_len


def calc_seen(seen: list[tuple[int, int, str]]) -> list[tuple[int, int]]:
    """
    Calculate the unique coordinates from the given list of tuples.

    Args:
        seen (list[tuple[int, int, str]]): The list of tuples containing coordinates.

    Returns:
        list[tuple[int, int]]: The list of unique coordinates.

    """
    ret = []
    for x in sorted(seen):
        coords = (x[0], x[1])
        if coords not in ret:
            ret.append(coords)
    return ret


# pylint:disable-next=too-many-branches
def move(
    lines: list[str],
    seen: list[tuple[int, int, str]],
    pos: tuple[int, int],
    direction: str,
) -> None:
    """
    Move function that recursively explores the grid based on the given position and direction.

    Args:
        lines (list[str]): The grid of characters.
        seen (list[tuple[int, int, str]]): List of previously visited positions.
        pos (tuple[int, int]): Current position in the grid.
        direction (str): Current direction of movement.

    Returns:
        None
    """
    next_pos = get_next_pos(pos, direction)

    if next_pos[0] < 0 or next_pos[1] < 0:
        return
    if next_pos[1] >= len(lines) or next_pos[0] >= len(lines[next_pos[1]]):
        return

    next_char = lines[next_pos[0]][next_pos[1]]
    next_seen = (next_pos[0], next_pos[1], direction)
    if next_char == "." and next_seen in seen:
        return

    if next_seen not in seen:
        seen.append(next_seen)

    if next_char == ".":
        move(lines, seen, next_pos, direction)

    if next_char == "-" and direction in ("right", "left"):
        move(lines, seen, next_pos, direction)
    if next_char == "|" and direction in ("right", "left"):
        move(lines, seen, next_pos, "up")
        move(lines, seen, next_pos, "down")

    if next_char == "|" and direction in ("up", "down"):
        move(lines, seen, next_pos, direction)
    if next_char == "-" and direction in ("up", "down"):
        move(lines, seen, next_pos, "left")
        move(lines, seen, next_pos, "right")

    if next_char == "/" and direction == "right":
        move(lines, seen, next_pos, "up")
    if next_char == "\\" and direction == "right":
        move(lines, seen, next_pos, "down")

    if next_char == "/" and direction == "left":
        move(lines, seen, next_pos, "down")
    if next_char == "\\" and direction == "left":
        move(lines, seen, next_pos, "up")

    if next_char == "/" and direction == "up":
        move(lines, seen, next_pos, "right")
    if next_char == "\\" and direction == "up":
        move(lines, seen, next_pos, "left")

    if next_char == "/" and direction == "down":
        move(lines, seen, next_pos, "left")
    if next_char == "\\" and direction == "down":
        move(lines, seen, next_pos, "right")


def get_next_pos(pos: tuple[int, int], direction: str) -> tuple[int, int]:
    """
    Calculates the next position based on the current position and direction.

    Args:
        pos (tuple[int, int]): The current position.
        direction (str): The current direction.

    Returns:
        tuple[int, int]: The next position.
    """
    if direction == "right":
        return (pos[0], pos[1] + 1)
    if direction == "left":
        return (pos[0], pos[1] - 1)
    if direction == "up":
        return (pos[0] - 1, pos[1])
    if direction == "down":
        return (pos[0] + 1, pos[1])

    raise ValueError("Invalid direction: " + direction)


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day16"))))
    print("Part two: " + str(part_two(util.get_lines("day16"))))
