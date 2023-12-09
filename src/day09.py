"""Advent of Code 2023 - Day 8 tasks"""

import re

# pylint: disable=import-error
if __package__ is None or not __package__:
    import util
else:
    from . import util


def part_one(lines):
    """
    Calculates the sum of the last values in each sequence obtained from the input lines.

    Args:
        lines (list): A list of strings representing the input lines.

    Returns:
        int: The sum of the last values in each sequence.
    """
    total = 0
    for line in lines:
        nums = list(map(int, re.findall(r'(-?\d+)', line)))  # Convert strings to integers
        sequences = get_sequences(nums)
        last_values = [seq[-1] for seq in sequences]  # Retrieve the last value from each sequence
        next_val = sum(last_values)
        total += next_val
    return total


def calc_differences(nums):
    """
    Calculate the differences between consecutive numbers in a list.

    Args:
        nums (list): A list of numbers.

    Returns:
        list: A list of differences between consecutive numbers.
    """
    differences = []
    for i in range(len(nums) - 1):
        differences.append(nums[i+1] - nums[i])
    return differences

def get_sequences(nums):
    """
    Get sequences of numbers by repeatedly calculating differences until all
    numbers in the sequence are the same.

    Args:
        nums (list): List of numbers.

    Returns:
        list: List of sequences, where each sequence is a list of numbers.
    """
    sequences = [nums]
    while not all(x == nums[0] for x in nums):
        nums = calc_differences(nums)
        sequences.append(nums)
    return sequences

if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines('day09'))))