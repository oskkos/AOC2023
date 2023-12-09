"""Advent of Code 2023 - Day 7 tasks"""

from typing import TypedDict

Hand = TypedDict(
    "Hand", {"bids": int, "cards": list[int], "hand": dict[str, list[int] | None]}
)

# pylint: disable=import-error
if not __package__:
    import util  # type: ignore
else:
    from . import util


def part_one(lines: list[str]) -> int:
    """
    part one
    """
    return calculate_bids(sort_hands(resolve_hands(lines, False)))


def part_two(lines: list[str]) -> int:
    """
    part two
    """
    return calculate_bids(sort_hands(resolve_hands(lines, True)))


# pylint: disable-next=too-many-return-statements
def map_to_number(char: str, joker: bool = False) -> int:
    """
    Maps a character to its corresponding number value.

    Args:
        char (str): The character to be mapped.
        joker (bool, optional): Whether the character is a joker. Defaults to False.

    Returns:
        int: The number value corresponding to the character.
    """
    if char == "A":
        return 14
    if char == "K":
        return 13
    if char == "Q":
        return 12
    if char == "J" and joker:
        return 1
    if char == "J":
        return 11
    if char == "T":
        return 10
    return int(char)


def resolve_hands(lines: list[str], joker: bool) -> list[Hand]:
    """
    Resolves the hands from the given lines and joker.

    Args:
        lines (list): List of strings representing the lines.
        joker (str): The joker character.

    Returns:
        list: List of dictionaries representing the resolved hands.
    """
    hands: list[Hand] = []
    for line in lines:
        cards = list(map(lambda char: map_to_number(char, joker), line.split(" ")[0]))
        bids = int(line.split(" ")[1])
        hands.append(Hand({"hand": group_hand(cards), "cards": cards, "bids": bids}))
    return hands


# pylint: disable-next=too-many-return-statements,too-many-branches
def group_hand(cards: list[int]) -> dict[str, list[int] | None]:
    """
    Group the cards in the hand and determine the best possible combination.

    Args:
        cards (str): A string representing the cards in the hand.

    Returns:
        dict: A dictionary representing the best possible combination of cards.
              The keys represent the combination type, and the values represent the card(s)
              involved.
              Possible combination types are:
              - 'FiveOfAKind': Represents a combination of five cards of the same rank.
              - 'FourOfAKind': Represents a combination of four cards of the same rank.
              - 'ThreeOfAKind': Represents a combination of three cards of the same rank.
              - 'TwoPairs': Represents a combination of two pairs of cards.
              - 'Pair': Represents a combination of two cards of the same rank.
              - 'FullHouse': Represents a combination of three cards of the same rank and a pair
                             of cards of the same rank.
              - 'HighCards': Represents a combination of high-ranking cards that do not form any
                             other combination.

              If no valid combination is found, an empty dictionary is returned.
    """
    groups: dict[int, int] = {}
    jokers = 0
    for card in cards:
        if card == 1:
            jokers += 1
        elif card not in groups:
            groups[card] = 1
        else:
            groups[card] += 1
    groups2: dict[str, list[int] | None] = {}
    items_sorted = sorted(groups.items(), key=lambda x: x[1], reverse=True)
    if jokers == 5:
        return {"FiveOfAKind": [0]}
    for card, group in items_sorted:
        if int(group) + jokers == 5:
            groups2["FiveOfAKind"] = [card]
        elif int(group) + jokers == 4:
            groups2["FourOfAKind"] = [card]
        elif int(group) + jokers == 3:
            groups2["ThreeOfAKind"] = [card]
        elif int(group) + jokers == 2:
            pairs: list[int] = groups2.get("Pair", [])  # type: ignore
            pairs.append(card)
            pairs.sort(reverse=True)
            if len(pairs) > 1:
                groups2["TwoPairs"] = pairs
            else:
                groups2["Pair"] = pairs
        else:
            high_cards = groups2.get("HighCards", [])
            if high_cards is not None:
                high_cards.append(card)
                high_cards.sort(reverse=True)
            groups2["HighCards"] = high_cards if high_cards is not None else []
        jokers = 0
    if groups2.get("FiveOfAKind"):
        return {"FiveOfAKind": groups2.get("FiveOfAKind")}
    if groups2.get("FourOfAKind"):
        return {"FourOfAKind": groups2.get("FourOfAKind")}
    if groups2.get("ThreeOfAKind") and groups2.get("Pair"):
        return {"FullHouse": [0]}
    if groups2.get("ThreeOfAKind"):
        return {"ThreeOfAKind": groups2.get("ThreeOfAKind")}
    if groups2.get("TwoPairs"):
        return {"TwoPairs": groups2.get("TwoPairs")}
    if groups2.get("Pair"):
        return {"Pair": groups2.get("Pair")}
    if groups2.get("HighCards"):
        return {"HighCards": groups2.get("HighCards")}
    return {}


def sort_hands(hands: list[Hand]) -> list[Hand]:
    """
    Sorts a list of hands based on their type and number of cards.

    Args:
        hands (list): A list of dictionaries representing hands, where each dictionary has
                      a 'hand' key indicating the type of hand and a 'cards' key indicating
                      the number of cards in the hand.

    Returns:
        list: A sorted list of hands, with hands of higher type and more cards appearing first.
    """
    five_of_a_kind_hands = [hand for hand in hands if "FiveOfAKind" in hand["hand"]]
    four_of_a_kind_hands = [hand for hand in hands if "FourOfAKind" in hand["hand"]]
    full_house_hands = [hand for hand in hands if "FullHouse" in hand["hand"]]
    three_of_a_kind_hands = [hand for hand in hands if "ThreeOfAKind" in hand["hand"]]
    two_pairs_hands = [hand for hand in hands if "TwoPairs" in hand["hand"]]
    pair_hands = [hand for hand in hands if "Pair" in hand["hand"]]
    high_cards_hands = [hand for hand in hands if "HighCards" in hand["hand"]]

    five_of_a_kind_hands.sort(key=lambda x: x["cards"], reverse=True)
    four_of_a_kind_hands.sort(key=lambda x: x["cards"], reverse=True)
    full_house_hands.sort(key=lambda x: x["cards"], reverse=True)
    three_of_a_kind_hands.sort(key=lambda x: x["cards"], reverse=True)
    two_pairs_hands.sort(key=lambda x: x["cards"], reverse=True)
    pair_hands.sort(key=lambda x: x["cards"], reverse=True)
    high_cards_hands.sort(key=lambda x: x["cards"], reverse=True)

    return (
        five_of_a_kind_hands
        + four_of_a_kind_hands
        + full_house_hands
        + three_of_a_kind_hands
        + two_pairs_hands
        + pair_hands
        + high_cards_hands
    )


def calculate_bids(hands_sorted: list[Hand]) -> int:
    """
    Calculate the total bids based on the given list of hands.

    Args:
        hands_sorted (list): A list of dictionaries representing hands, where each dictionary
                             contains the 'bids' key indicating the number of bids for that hand.

    Returns:
        int: The total bids calculated based on the given list of hands.
    """
    total: int = 0
    for i, hand in enumerate(hands_sorted):
        total += hand["bids"] * (len(hands_sorted) - i)
    return total


if __name__ == "__main__":
    file_lines = util.get_lines("day07")
    print("Part one: " + str(part_one(file_lines)))
    print("Part two: " + str(part_two(file_lines)))
