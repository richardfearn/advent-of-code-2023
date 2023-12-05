import re
from collections import namedtuple

Card = namedtuple("Card", ["number", "matches"])


def part_1_answer(lines):
    cards = parse_cards(lines)
    return sum(point_value(card) for card in cards)


def point_value(card):
    return 0 if (card.matches == 0) else (1 << (card.matches - 1))


def part_2_answer(lines):
    cards = parse_cards(lines)
    copies = [1] * len(cards)

    for card in cards:
        for i in range(card.number + 1, card.number + card.matches + 1):
            copies[i - 1] += copies[card.number - 1]

    return sum(copies)


def parse_cards(lines) -> list[Card]:
    return [parse_card(line) for line in lines]


def parse_card(line):
    card_num, numbers = line.split(": ")

    card_num = int(re.findall(r"\d+", card_num)[0])

    winning_numbers, numbers_you_have = numbers.split("|")
    winning_numbers = set(int(n) for n in re.findall(r"\d+", winning_numbers))
    numbers_you_have = set(int(n) for n in re.findall(r"\d+", numbers_you_have))

    num_matches = len(winning_numbers & numbers_you_have)

    return Card(card_num, num_matches)
