"""Advent of Code 2023 - Day 9 tasks"""


# pylint: disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    Calculates the total number of paths between points in a galaxy map.

    Args:
        lines (list[str]): The lines representing the galaxy map.

    Returns:
        int: The total number of paths between points.
    """
    lines = expand_lines(lines)
    galaxy_map = build_galaxy_map(lines)

    paths = 0
    for g, (x1, y1) in galaxy_map.items():
        for g2, (x2, y2) in galaxy_map.items():
            if g2 <= g:
                continue
            paths += abs(x1 - x2) + abs(y1 - y2)
    return paths


def expand_lines(lines: list[str]) -> list[str]:
    """
    Expands the lines by adding dots ('.') to rows and columns that contain only dots.

    Args:
        lines (list[str]): The list of lines to expand.

    Returns:
        list[str]: The expanded list of lines.
    """
    dot_rows = []
    for i, line in enumerate(lines):
        if all(char == "." for char in line):
            dot_rows.append(i)

    dot_cols = []
    cols_length = len(lines[0])
    for i in range(cols_length):
        if all(line[i] == "." for line in lines):
            dot_cols.append(i)

    for row in reversed(dot_rows):
        lines.insert(row, "." * len(lines[0]))  # Add new line at the position of row

    for col in reversed(dot_cols):
        for i, line in enumerate(lines):
            lines[i] = line[:col] + "." + line[col:]  # Insert dot at the position of col
    return lines


def build_galaxy_map(lines: list[str]) -> dict[int, tuple[int, int]]:
    """
    Builds a galaxy map based on the given lines.

    Args:
        lines (list[str]): The lines representing the galaxy map.

    Returns:
        dict[int, tuple[int, int]]: A dictionary mapping galaxy numbers to their coordinates.
    """
    galaxy_nbr = 0
    galaxy_map = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                galaxy_nbr += 1
                galaxy_map[galaxy_nbr] = (i, j)
    return galaxy_map


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day11"))))
    # print("Part two: " + str(part_two(util.get_lines("temp"))))
