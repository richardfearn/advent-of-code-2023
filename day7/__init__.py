TYPE_PREDICATES = [

    # Five of a kind
    lambda counts: len(counts) == 1,

    # Four of a kind
    lambda counts: set(counts.values()) == {1, 4},

    # Full house
    lambda counts: set(counts.values()) == {2, 3},

    # Three of a kind
    lambda counts: (3 in counts.values()) and (len(counts) == 3),

    # Two pair
    lambda counts: (len(counts) == 3) and (set(counts.values()) == {1, 2}),

    # One pair
    lambda counts: (len(counts) == 4) and (2 in counts.values()),

    # High card
    lambda counts: len(counts) == 5,
]


class Hand:
    # pylint: disable=too-few-public-methods
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.type = None
        self.rank = None
        self.win_amount = None


def part_1_answer(lines):
    hands = parse(lines)

    for hand in hands:
        hand.type = hand_type(hand.hand)

    return total_winnings(hands, "AKQJT98765432")


def part_2_answer(lines):
    hands = parse(lines)

    for hand in hands:
        hand.type = strongest_type(hand.hand)

    return total_winnings(hands, "AKQT98765432J")


def hand_type(hand):
    card_counts = {card: hand.count(card) for card in set(hand)}
    return next(i for (i, predicate) in enumerate(TYPE_PREDICATES) if predicate(card_counts))


def total_winnings(hands, card_order):
    hands.sort(key=lambda h: (-h.type, [-card_order.index(c) for c in h.hand]))

    for i, hand in enumerate(hands):
        hand.rank = i + 1
        hand.win_amount = hand.bid * hand.rank

    return sum(hand.win_amount for hand in hands)


def strongest_type(hand):
    return min(hand_type(hand.replace("J", card)) for card in "AKQT98765432")


def parse(lines):
    lines = [line.split(" ") for line in lines]
    return [Hand(line[0], int(line[1])) for line in lines]
