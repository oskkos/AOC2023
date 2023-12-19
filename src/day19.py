"""Advent of Code 2023 - Day 19 tasks"""


# pylint:disable=import-error
import re


if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    Calculate the total based on the ratings of the workflows.

    Args:
        lines (list[str]): The input lines containing workflow and rating strings.

    Returns:
        int: The total calculated based on the ratings.

    """
    workflow_strs, rating_strs = lines_to_workflows_and_ratings_strings(lines)
    workflows = parse_workflows(workflow_strs)
    ratings = parse_ratings(rating_strs)

    total = 0
    for rating in ratings:
        if (run_workflow(rating, workflows, "in", 0)) == "A":
            total += sum(rating)
    return total


def run_workflow(
    ratings: list[int],
    workflows: dict[str, list[list[str]]],
    name: str,
    pos: int,
) -> str:
    """
    Executes a workflow based on the given ratings, workflows, name, and position.

    Args:
        ratings (list[int]): The ratings used in the workflow.
        workflows (dict[str, list[list[str]]]): The dictionary of workflows.
        name (str): The name of the workflow to execute.
        pos (int): The position of the current step in the workflow.

    Returns:
        str: The result of executing the workflow.

    """
    # x,m,a,s are used in eval
    # pylint:disable-next=unused-variable
    x, m, a, s = ratings
    cmd = workflows[name][pos][0]
    if cmd in ("A", "R"):
        return cmd
    if cmd in workflows:
        return run_workflow(ratings, workflows, cmd, 0)
    # pylint:disable-next=eval-used
    if eval(cmd):
        next_step = workflows[name][pos][1]
        if next_step in ("A", "R"):
            return next_step
        return run_workflow(ratings, workflows, next_step, 0)
    return run_workflow(ratings, workflows, name, pos + 1)


def lines_to_workflows_and_ratings_strings(
    lines: list[str],
) -> tuple[list[str], list[str]]:
    """
    Convert a list of lines into separate lists for workflows and ratings.

    Args:
        lines (list[str]): The input list of lines.

    Returns:
        tuple[list[str], list[str]]: A tuple containing two lists:
            - workflows: A list of workflow strings.
            - ratings: A list of rating strings.
    """
    workflows: list[str] = []
    ratings: list[str] = []
    current: list[str] = workflows
    for line in lines:
        if not line:
            current = ratings
        else:
            current.append(line)
    return workflows, ratings


def parse_workflows(workflow_strs: list[str]) -> dict[str, list[list[str]]]:
    """
    Parses a list of workflow strings and returns a dictionary of workflows.

    Args:
        workflow_strs (list[str]): A list of workflow strings.

    Returns:
        dict[str, list[list[str]]]: A dictionary where the keys are workflow names and the
                                    values are lists of rules.

    Example:
        workflow_strs = [
            "Workflow1{rule1:chunk1,rule2:chunk2}",
            "Workflow2{rule3:chunk3,rule4:chunk4}"
        ]
        parse_workflows(workflow_strs) returns:
        {
            "Workflow1": [["rule1", "chunk1"], ["rule2", "chunk2"]],
            "Workflow2": [["rule3", "chunk3"], ["rule4", "chunk4"]]
        }
    """
    workflows = {}
    for workflow_str in workflow_strs:
        workflow = []
        workflow_name = workflow_str.split("{")[0]
        rules = workflow_str.split("{")[1].split("}")[0].split(",")
        for rule in rules:
            chunks = rule.split(":")
            workflow.append(chunks)
        workflows[workflow_name] = workflow
    return workflows


def parse_ratings(rating_strs: list[str]) -> list[list[int]]:
    """
    Parse a list of rating strings and convert them into a list of lists of integers.

    Args:
        rating_strs (list[str]): A list of rating strings.

    Returns:
        list[list[int]]: A list of lists of integers representing the parsed ratings.
    """
    ratings = []
    for rating in rating_strs:
        ratings.append(list(map(int, re.findall(r"\d+", rating))))
    return ratings


if __name__ == "__main__":
    print("Part one: " + str(part_one(util.get_lines("day19"))))
    # print("Part two: " + str(part_two(util.get_lines("day18"))))
