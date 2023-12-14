"""Advent of Code 2023 - Day 11 tasks"""


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
    return part_two(lines, 2)


# pylint: disable-next=too-many-locals
def part_two(lines: list[str], dot_row_or_col_multiplier: int) -> int:
    """
    Calculates the number of paths between dots in a galaxy map.

    Args:
        lines (list[str]): The lines representing the galaxy map.
        dot_row_or_col_multiplier (int): The multiplier for paths between
                                         dots in the same row or column.

    Returns:
        int: The total number of paths between dots in the galaxy map.
    """
    dot_rows, dot_cols = get_dot_rows_and_cols(lines)
    galaxy_map = build_galaxy_map(lines)

    paths = 0
    for g, (x1, y1) in galaxy_map.items():
        for g2, (x2, y2) in galaxy_map.items():
            if g2 <= g:
                continue
            from_row = min(x1, x2)
            to_row = max(x1, x2)
            from_col = min(y1, y2)
            to_col = max(y1, y2)

            for i in range(from_row + 1, to_row + 1):
                if i in dot_rows:
                    paths += dot_row_or_col_multiplier
                else:
                    paths += 1
            for i in range(from_col + 1, to_col + 1):
                if i in dot_cols:
                    paths += dot_row_or_col_multiplier
                else:
                    paths += 1
    return paths


def get_dot_rows_and_cols(lines: list[str]) -> tuple[list[int], list[int]]:
    """
    Gets the rows and columns that contain only dots.

    Args:
        lines (list[str]): The lines to check.

    Returns:
        tuple[list[int], list[int]]: A tuple containing the rows and columns that contain
                                     only dots.
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
    return dot_rows, dot_cols


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
    print("Part two: " + str(part_two(util.get_lines("day11"), 1000000)))
