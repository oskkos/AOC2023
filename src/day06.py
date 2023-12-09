"""Advent of Code 2023 - Day 6 tasks"""

import re

# pylint: disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    part one
    """
    total = 1
    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])
    for i, time in enumerate(times):
        min_time = calc_min_hold_time(int(time), int(distances[i]))
        max_time = calc_max_hold_time(int(time), int(distances[i]))
        total = total * len(range(min_time, max_time + 1))
    return total


def part_two(lines: list[str]) -> int:
    """
    part two
    """

    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])
    time = ""
    distance = ""
    for i, xx in enumerate(times):
        time += xx
        distance += distances[i]
    min_time = calc_min_hold_time(int(time), int(distance))
    max_time = calc_max_hold_time(int(time), int(distance))
    total = len(range(min_time, max_time + 1))
    return total


def calc_min_hold_time(time: int, distance: int) -> int:
    """
    Calculates the minimum hold time required to travel a given distance within a given time.

    Args:
        time (int): The total time available for travel.
        distance (int): The distance that needs to be traveled.

    Returns:
        int: The minimum hold time required to travel the distance within the given time.
             Returns -1 if it is not possible to travel the distance within the given time.
    """
    min_hold_time = 1
    while min_hold_time <= time:
        speed = min_hold_time
        remainder = time - min_hold_time
        distance_traveled = speed * remainder
        if distance_traveled > distance:
            return min_hold_time
        min_hold_time += 1
    return -1


def calc_max_hold_time(time: int, distance: int) -> int:
    """
    Calculates the maximum hold time for a given time and distance.

    Args:
        time (int): The total time available for holding.
        distance (int): The distance that needs to be traveled.

    Returns:
        int: The maximum hold time that allows the distance to be traveled within the given time.
             Returns -1 if it is not possible to travel the distance within the given time.
    """
    max_hold_time = time
    while max_hold_time > 0:
        speed = max_hold_time
        remainder = time - max_hold_time
        distance_traveled = speed * remainder
        if distance_traveled > distance:
            return max_hold_time
        max_hold_time -= 1
    return -1


if __name__ == "__main__":
    file_lines = util.get_lines("day06")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
