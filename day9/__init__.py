from itertools import pairwise


def part_1_answer(lines):
    histories = [[int(n) for n in line.split(" ")] for line in lines]
    return sum(part_1_predict(history) for history in histories)


def part_2_answer(lines):
    histories = [[int(n) for n in line.split(" ")] for line in lines]
    return sum(part_2_predict(history) for history in histories)


def part_1_predict(history):
    sequences = [history]
    while set(sequences[-1]) != {0}:
        sequences.append(next_sequence(sequences[-1]))
    for lower, upper in pairwise(reversed(sequences)):
        upper.append(upper[-1] + lower[-1])
    return sequences[0][-1]


def part_2_predict(history):
    sequences = [history]
    while set(sequences[-1]) != {0}:
        sequences.append(next_sequence(sequences[-1]))
    for lower, upper in pairwise(reversed(sequences)):
        upper.insert(0, upper[0] - lower[0])
    return sequences[0][0]


def next_sequence(numbers):
    return [(b - a) for (a, b) in pairwise(numbers)]
