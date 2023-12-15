"""Advent of Code 2023 - Day 15 tasks"""


from typing import NewType, TypedDict

# pylint:disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


Box = TypedDict("Box", {"label": str, "len": int})

Boxes = NewType("Boxes", dict[int, list[Box]])


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


def part_two(lines: list[str]) -> int:
    """
    Calculates the result for part two of the problem.

    Args:
        lines (list[str]): The input lines.

    Returns:
        int: The result for part two.
    """
    boxes: dict[int, list[Box]] = {}
    for i in range(256):
        boxes[i] = []

    for line in lines:
        chunks = line.split(",")
        for chunk in chunks:
            splitter = "=" if chunk.find("=") != -1 else "-"
            label = chunk[: chunk.find(splitter)]
            box_nbr = get_chunk_val(label)

            if splitter == "=":
                focal_len = int(chunk[chunk.find(splitter) + 1 :])
                handle_add_to_box(boxes, box_nbr, label, focal_len)
            elif splitter == "-":
                handle_remove_from_box(boxes, box_nbr, label)

    total = 0
    for box_nbr, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            lenses_in_box_sum = int(box_nbr + 1) * (i + 1) * lens["len"]
            total += lenses_in_box_sum

    return total


def handle_add_to_box(
    boxes: dict[int, list[Box]], box: int, label: str, focal_len: int
) -> None:
    """
    Add or update a label with its focal length to a specific box.

    Args:
        boxes (list): The list of boxes.
        box (int): The index of the box to add/update the label in.
        label (str): The label to add/update.
        focal_len (int): The focal length to associate with the label.

    Returns:
        None
    """
    labels = boxes[box]
    replace = False
    for label_dict in labels:
        if label_dict["label"] == label:
            label_dict["len"] = focal_len
            replace = True
            break
    if not replace:
        boxes[box].append({"label": label, "len": focal_len})


def handle_remove_from_box(boxes: dict[int, list[Box]], box: int, label: str) -> None:
    """
    Remove a label from a box.

    Args:
        boxes (dict): A dictionary containing boxes and their labels.
        box (str): The box from which the label should be removed.
        label (str): The label to be removed.

    Returns:
        None
    """
    labels = boxes[box]
    for label_dict in labels:
        if label_dict["label"] == label:
            labels.remove(label_dict)
            break


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
        total += get_chunk_val(chunk)

    return total


def get_chunk_val(chunk: str) -> int:
    """
    Get the value of a chunk.

    Returns:
        int: The value of the chunk.
    """
    chunk_val = 0
    for char in chunk:
        ascii_code = ord(char)
        chunk_val += ascii_code
        chunk_val *= 17
        chunk_val %= 256
    return chunk_val


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day15"))))
    print("Part two: " + str(part_two(util.get_lines("day15"))))
