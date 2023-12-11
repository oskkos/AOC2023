"""Advent of Code 2023 - Day 9 tasks"""

import math

# pylint: disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    Calculate the number of moves required to return to the starting position.

    Args:
        lines (list[str]): The list of input lines.

    Returns:
        int: The number of moves required.
    """
    s_coords = resolve_start_pos(lines)
    next_pos = resolve_start_direction(s_coords, lines)

    moves = 0
    while next_pos is not None and next_pos[:2] != s_coords:
        moves += 1
        next_pos = move(next_pos, lines)

    return int(math.ceil(moves / 2))


def part_two(lines: list[str]) -> int:
    """
    Counts the number of inside characters in a grid based on the given lines.

    Args:
        lines (list[str]): The lines representing the grid.

    Returns:
        int: The count of inside characters.

    """
    s_coords = resolve_start_pos(lines)
    next_pos = resolve_start_direction(s_coords, lines)

    seen: dict[int, dict[int, bool]] = {}

    a = seen.get(s_coords[0], {})
    a[s_coords[1]] = True
    seen[s_coords[0]] = a

    moves = 0
    while next_pos is not None and next_pos[:2] != s_coords:
        a = seen.get(next_pos[0], {})
        a[next_pos[1]] = True
        seen[next_pos[0]] = a

        moves += 1
        next_pos = move(next_pos, lines)

    inside_chars = 0
    for i, line in enumerate(lines):
        inside = False
        angle = ""
        for j, char in enumerate(line):
            seen_char = is_seen(i, j, seen)
            angle, inside = handle_angle(seen_char, char, angle, inside)

            if seen_char and char == "|":
                inside = not inside
            elif not seen_char and inside:
                inside_chars += 1

    return inside_chars


def handle_angle(seen_char: bool, char: str, angle: str, inside: bool) -> tuple[str, bool]:
    """
    Handle the angle based on the given parameters.

    Args:
        seen_char (bool): Indicates if a character has been seen.
        char (str): The character to be processed.
        angle (str): The current angle.
        inside (bool): Indicates if the current position is inside.

    Returns:
        tuple[str, bool]: The updated angle and inside status.
    """
    if seen_char and char == "F" and not angle:
        angle = "F"
    if seen_char and char == "7" and angle == "F":
        angle = ""
    if seen_char and char == "J" and angle == "F":
        angle = ""
        inside = not inside

    if seen_char and char == "L" and not angle:
        angle = "L"
    if seen_char and char == "J" and angle == "L":
        angle = ""
    if seen_char and char == "7" and angle == "L":
        angle = ""
        inside = not inside
    return angle, inside


def is_seen(i: int, j: int, seen: dict[int, dict[int, bool]]) -> bool:
    """
    Check if a specific element is seen in the 'seen' dictionary.

    Args:
        i (int): The first key of the 'seen' dictionary.
        j (int): The second key of the nested dictionary inside 'seen'.
        seen (dict[int, dict[int, bool]]): The dictionary to check.

    Returns:
        bool: True if the element is seen, False otherwise.
    """
    return seen.get(i, {}).get(j, False)


def resolve_start_pos(lines: list[str]) -> tuple[int, int]:
    """
    Finds the position of the character 'S' in the given lines.

    Args:
        lines (list[str]): The lines to search for the character 'S'.

    Returns:
        tuple[int, int]: The row and column indices of the character 'S' if found,
                         otherwise (-1, -1).
    """
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                return i, j
    return -1, -1  # Return -1, -1 if 'S' is not found in the lines


def resolve_start_direction(
    s_coords: tuple[int, int],
    lines: list[str],
) -> tuple[int, int, str] | None:
    """
    Resolves the starting direction based on the given coordinates and lines.

    Args:
        s_coords (tuple[int, int]): The starting coordinates.
        lines (list[str]): The lines containing the directions.

    Returns:
        tuple[int, int, str] | None: A tuple containing the updated coordinates and the
        next direction, or None if no valid direction is found.
    """
    i, j = s_coords
    if "-J7".find(lines[i][j + 1]) != -1:
        return (i, j + 1, next_direction(s_coords, (i, j + 1), lines))
    if "-LF".find(lines[i][j - 1]) != -1:
        return (i, j - 1, next_direction(s_coords, (i, j - 1), lines))
    if "|LJ".find(lines[i + 1][j]) != -1:
        return (i + 1, j, next_direction(s_coords, (i + 1, j), lines))
    if "|7F".find(lines[i - 1][j]) != -1:
        return (i - 1, j, next_direction(s_coords, (i - 1, j), lines))
    return None


def next_direction(
    current: tuple[int, int],
    next_pos: tuple[int, int],
    lines: list[str],
) -> str:
    """
    Determines the next direction based on the current position and the next position.

    Args:
        current (tuple[int, int]): The current position as a tuple of (row, column).
        next_pos (tuple[int, int]): The next position as a tuple of (row, column).
        lines (list[str]): The lines representing the grid.

    Returns:
        str: The next direction as a string ("up", "down", "left", or "right").
    """
    i, j = current
    ii, jj = next_pos

    direction: str = ""
    char = lines[ii][jj]
    if char == "|" and i + 1 == ii and j == jj:
        direction = "down"
    elif char == "|" and i - 1 == ii and j == jj:
        direction = "up"
    elif char == "-" and i == ii and j + 1 == jj:
        direction = "right"
    elif char == "-" and i == ii and j - 1 == jj:
        direction = "left"
    elif char == "L" and i + 1 == ii and j == jj:
        direction = "right"
    elif char == "L" and i == ii and j - 1 == jj:
        direction = "up"
    elif char == "J" and i + 1 == ii and j == jj:
        direction = "left"
    elif char == "J" and i == ii and j + 1 == jj:
        direction = "up"
    elif char == "7" and i - 1 == ii and j == jj:
        direction = "left"
    elif char == "7" and i == ii and j + 1 == jj:
        direction = "down"
    elif char == "F" and i - 1 == ii and j == jj:
        direction = "right"
    elif char == "F" and i == ii and j - 1 == jj:
        direction = "down"
    return direction


def move(
    coords: tuple[int, int, str],
    lines: list[str],
) -> tuple[int, int, str] | None:
    """
    Move the coordinates in the specified direction and return the updated coordinates.

    Args:
        coords (tuple[int, int, str]): The current coordinates (i, j, direction).
        lines (list[str]): The lines representing the grid.

    Returns:
        tuple[int, int, str] | None: The updated coordinates (i, j, direction) if the move is valid,
        None otherwise.
    """
    i, j, direction = coords
    if direction == "right":
        return i, j + 1, next_direction((i, j), (i, j + 1), lines)
    if direction == "left":
        return i, j - 1, next_direction((i, j), (i, j - 1), lines)
    if direction == "up":
        return i - 1, j, next_direction((i, j), (i - 1, j), lines)
    if direction == "down":
        return i + 1, j, next_direction((i, j), (i + 1, j), lines)
    return None


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day10"))))
    print("Part two: " + str(part_two(util.get_lines("day10"))))
