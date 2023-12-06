"""Advent of Code 2023 - Day 5 tasks"""

import re

# pylint: disable=import-error
if __package__ is None or not __package__:
    import util
else:
    from . import util


def part_one(lines):
    """
    part one
    """
    return runner(lines, False)
def part_two(lines):
    """
    part one
    """
    return runner(lines, True)

def runner(lines, seeds_as_range):
    """
    Runs the mapping algorithm based on the given lines and seeds.

    Args:
        lines (list): List of lines containing mapping information.
        seeds_as_range (bool): Flag indicating whether seeds are given as ranges.

    Returns:
        int: The minimum location value obtained from the mapping algorithm.
    """
    seeds =[]
    mapping = {}
    current_map = ''
    for line in lines:
        if line.split(':')[0] == 'seeds':
            seeds = get_seeds(line, seeds_as_range)
            continue
        current_map = resolve_current_map(current_map, line)
        map_values = re.findall(r'\d+', line)
        update_mapping(mapping, current_map, map_values)
    locations = []
    for _, seed in enumerate(seeds):
        if isinstance(seed, range):
            #print(f"range: {_+1}/{len(seeds)}, {seed}")
            locations.extend([traverse_mapping(mapping, x) for x in seed])
        else:
            locations.append(traverse_mapping(mapping, int(seed)))
    return min(locations)


def traverse_mapping(mapping, seed):
    """
    Traverses the mapping to determine the location based on the given seed.

    Args:
        mapping (dict): A dictionary containing the mapping between different stages of growth.
        seed (int): The seed value to start the traversal.

    Returns:
        str: The location determined by the traversal.

    """
    #print(f"traversing {seed}") if seed % 1000 == 0 else None
    soil = get_destination(mapping['seed-to-soil'], seed)
    fertilizer = get_destination(mapping['soil-to-fertilizer'], soil)
    water = get_destination(mapping['fertilizer-to-water'], fertilizer)
    light = get_destination(mapping['water-to-light'], water)
    temperature = get_destination(mapping['light-to-temperature'], light)
    humidity = get_destination(mapping['temperature-to-humidity'], temperature)
    location = get_destination(mapping['humidity-to-location'], humidity)
    return location

# pylint: disable-next=too-many-return-statements
def resolve_current_map(current_map, line):
    """
    Resolves the current map based on the given line.

    Args:
        current_map (str): The current map.
        line (str): The line to be checked.

    Returns:
        str: The resolved map based on the line.
    """
    if line.strip() == 'seed-to-soil map:':
        return 'seed-to-soil'
    if line.strip() == 'soil-to-fertilizer map:':
        return 'soil-to-fertilizer'
    if line.strip() == 'fertilizer-to-water map:':
        return 'fertilizer-to-water'
    if line.strip() == 'water-to-light map:':
        return 'water-to-light'
    if line.strip() == 'light-to-temperature map:':
        return 'light-to-temperature'
    if line.strip() == 'temperature-to-humidity map:':
        return 'temperature-to-humidity'
    if line.strip() == 'humidity-to-location map:':
        return 'humidity-to-location'
    return current_map

def update_mapping(mapping, current_map, values):
    """
    Update the mapping dictionary with the given values for the current_map.

    Args:
        mapping (dict): The mapping dictionary to update.
        current_map (str): The key for the current map in the mapping dictionary.
        values (list): A list of three values: destination, source, and length.

    Returns:
        None
    """
    if len(values) != 3:
        return
    current_map_mapping = mapping.get(current_map, {})
    destination, source, length = values
    current_map_mapping[int(source)] = {"destination": int(destination), "length": int(length)}
    mapping[current_map] = current_map_mapping

def get_destination(mapping, source):
    """
    Get the destination corresponding to the given source based on the provided mapping.

    Args:
        mapping (dict): A dictionary mapping source values to destination values.
        source: The source value for which to find the corresponding destination.

    Returns:
        The destination value corresponding to the given source, or None if no mapping is found.
    """
    for source_candidate in mapping.keys():
        if source in range(source_candidate, source_candidate+mapping[source_candidate]["length"]):
            return source - source_candidate + mapping[source_candidate]["destination"]
    return source

def get_seeds(seeds_line, ranges):
    """
    Extracts seeds from a line and returns them as a list of integers.

    Parameters:
    seeds_line (str): The line containing the seeds.
    ranges (bool): Flag indicating whether to return seed ranges or individual seeds.

    Returns:
    list: A list of integers representing the seeds.
    """
    nums = re.findall(r'\d+', seeds_line.split(':')[1])
    if not ranges:
        return nums

    seed_ranges = []
    for i in range(0, len(nums), 2):
        seed_range = range(int(nums[i]), int(nums[i]) + int(nums[i+1]))
        seed_ranges.append(seed_range)
    return seed_ranges


if __name__ == "__main__":
    file_lines = util.get_lines('day05')
    print("Part one: " + str(part_one(file_lines)))
    #print("Part two: " + str(part_two(file_lines))) # this takes ages :-/
