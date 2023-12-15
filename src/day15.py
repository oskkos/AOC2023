"""Advent of Code 2023 - Day 15 tasks"""


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
    total = 0
    for line in lines:
        total += calculate_total(line.split(","))
    return total


def calculate_total(chunks: list[str]) -> int:
    """
    Calculate the total value of a list of chunks.

    Args:
        chunks (list[str]): A list of chunks.

    Returns:
        int: The total value of the chunks.
    """
    total = 0
    for chunk in chunks:
        chunk_val = 0
        for char in chunk:
            ascii_code = ord(char)
            chunk_val += ascii_code
            chunk_val *= 17
            chunk_val %= 256
        print(f"{chunk} = {chunk_val}")
        total += chunk_val

    return total


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day15"))))
    # print("Part two: " + str(part_two(util.get_lines("day14")))) # too slow, took 3 hours :-/
