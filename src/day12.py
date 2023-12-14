# pylint:disable=missing-module-docstring
import functools

# pylint:disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    Calculates the total number of possibilities for each line in the given list of strings.

    Args:
        lines (list[str]): A list of strings representing each line.

    Returns:
        int: The total number of possibilities.

    """
    total = 0
    for line in lines:
        row_and_sizes = line.split()
        row = row_and_sizes[0]
        sizes = tuple(map(int, row_and_sizes[1].split(",")))
        total += count_possibilities(row + ".", sizes)
    return total


def part_two(lines: list[str]) -> int:
    """
    Calculates the total number of possibilities based on the given lines.

    Args:
        lines (list[str]): The input lines.

    Returns:
        int: The total number of possibilities.
    """
    total = 0
    for line in lines:
        row_and_sizes = line.split()
        row = row_and_sizes[0]
        sizes = tuple(map(int, row_and_sizes[1].split(",")))
        total += count_possibilities("?".join([row] * 5) + ".", sizes * 5)
    return total


@functools.cache
def count_possibilities(
    row_str: str,
    group_sizes: tuple[int],
    handled_chars_in_group: int = 0,
) -> int:
    """
    Count the number of possibilities for a given row string, group sizes, and number of
    symbols done in a group.

    Args:
        row_str (str): The row string representing the symbols in the row.
        group_sizes (tuple[int]): The sizes of the groups.
        handled_chars_in_group (int, optional): The number of symbols done in the current group.
        Defaults to 0.

    Returns:
        int: The number of possibilities for the given row string, group sizes, and number of
        symbols in a group.
    """
    if not row_str:
        # End of the row and nothing unhandled in the group
        return int(not group_sizes and not handled_chars_in_group)

    count = 0
    char_options = [".", "#"] if row_str[0] == "?" else row_str[0]
    for char in char_options:
        if char == "#":
            # Extend ongoing group
            count += count_possibilities(
                row_str[1:], group_sizes, handled_chars_in_group + 1
            )
        else:
            if handled_chars_in_group:
                if group_sizes and group_sizes[0] == handled_chars_in_group:
                    # group is full, move on to next group
                    count += count_possibilities(row_str[1:], group_sizes[1:])
            else:
                # not in a group, advance to next char
                count += count_possibilities(row_str[1:], group_sizes)
    return count


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day12"))))
    print("Part two: " + str(part_two(util.get_lines("day12"))))
