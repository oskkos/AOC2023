"""Advent of Code 2023 - Day 16 tasks"""


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
    trench_map: dict[int, dict[int, bool]] = {}
    trench_map[0] = {0: True}
    current_position = (0, 0)
    for line in lines:
        instructions = line.split()
        direction = instructions[0]
        meters = int(instructions[1])
        current_position = add_to_trench_map(
            trench_map, current_position, direction, meters
        )
    return render_trench(trench_map)


def part_two(lines: list[str]) -> int:
    """
    Calculates the result for part two of the problem.

    Args:
        lines (list[str]): The input lines.

    Returns:
        int: The result for part one.
    """
    trench_map: dict[int, dict[int, bool]] = {}
    trench_map[0] = {0: True}
    current_position = (0, 0)
    for line in lines:
        instructions = line.split("(")[1].split(")")[0]
        meters = int(instructions[1:-1], 16)
        direction_int = int(instructions[-1])
        direction = int_to_direction(direction_int)
        current_position = add_to_trench_map(
            trench_map, current_position, direction, meters
        )
    return 0
    # return render_trench(trench_map) # this will take too long :-/


def int_to_direction(direction_int: int) -> str:
    """
    Converts an integer representation of a direction to a string representation.

    Args:
        direction_int (int): The integer representation of the direction.
            - 0: Right (R)
            - 1: Down (D)
            - 2: Left (L)
            - 3: Up (U)

    Returns:
        str: The string representation of the direction.

    """
    return (
        "R"
        if not direction_int
        else "D"
        if direction_int == 1
        else "L"
        if direction_int == 2
        else "U"
    )


def add_to_trench_map(
    trench_map: dict[int, dict[int, bool]],
    current_position: tuple[int, int],
    direction: str,
    meters: int,
) -> tuple[int, int]:
    """
    Adds a path to the trench map based on the given direction and meters.

    Args:
        trench_map (dict[int, dict[int, bool]]): The trench map.
        current_position (tuple[int, int]): The current position on the map.
        direction (str): The direction to move in ("U" for up, "D" for down,
                         "L" for left, "R" for right).
        meters (int): The number of meters to move in the given direction.

    Returns:
        tuple[int, int]: The new current position after moving.

    """
    if direction == "U":
        for _ in range(meters):
            current_position = (current_position[0] - 1, current_position[1])
            if current_position[0] not in trench_map:
                trench_map[current_position[0]] = {}
            trench_map[current_position[0]][current_position[1]] = True
    if direction == "D":
        for _ in range(meters):
            current_position = (current_position[0] + 1, current_position[1])
            if current_position[0] not in trench_map:
                trench_map[current_position[0]] = {}
            trench_map[current_position[0]][current_position[1]] = True
    if direction == "L":
        for _ in range(meters):
            current_position = (current_position[0], current_position[1] - 1)
            if current_position[0] not in trench_map:
                trench_map[current_position[0]] = {}
            trench_map[current_position[0]][current_position[1]] = True
    if direction == "R":
        for _ in range(meters):
            current_position = (current_position[0], current_position[1] + 1)
            if current_position[0] not in trench_map:
                trench_map[current_position[0]] = {}
            trench_map[current_position[0]][current_position[1]] = True
    return current_position


def render_trench(trench_map: dict[int, dict[int, bool]]) -> int:
    """
    Renders the trench map and returns the count of rendered elements.

    Args:
        trench_map (dict[int, dict[int, bool]]): A dictionary representing the trench map,
            where the keys are row numbers and the values are dictionaries representing the
            columns and their corresponding boolean values.

    Returns:
        int: The count of rendered elements.

    """
    rows = sorted(trench_map.keys())
    count = 0
    for row in rows:
        cols = trench_map[row].keys()
        inside = False
        edge_begin: int | None = None
        for col in range(max(cols) + 1):
            if col in cols:
                if edge_begin is None:
                    edge_begin = col
                else:
                    if (
                        exists(trench_map, row - 1, col)
                        and exists(trench_map, row - 1, edge_begin)
                    ) or (
                        exists(trench_map, row + 1, col)
                        and exists(trench_map, row + 1, edge_begin)
                    ):
                        edge_begin = None

                # print("#", end="")
                count += 1
            else:
                if edge_begin is not None:
                    inside = not inside
                    edge_begin = None
                if inside:
                    # print("+", end="")
                    count += 1
                else:
                    pass
                    # print(".", end="")
        # print()
    return count


def exists(trench_map: dict[int, dict[int, bool]], row: int, col: int) -> bool:
    """
    Check if a given row and column exists in the trench map.

    Args:
        trench_map (dict[int, dict[int, bool]]): The trench map.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if the row and column exist in the trench map, False otherwise.
    """
    if row not in trench_map:
        return False
    if col not in trench_map[row]:
        return False
    return True


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day18"))))
    print("Part two: " + str(part_two(util.get_lines("day18"))))
