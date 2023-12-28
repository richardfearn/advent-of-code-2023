import re
from itertools import combinations
from functools import cache


def part_1_answer(lines):
    records = [parse(line) for line in lines]
    return sum(combination_arrangements(record) for record in records)


def combination_arrangements(record):
    conditions, groups = record

    num_damaged = sum(groups)
    num_damaged_known = conditions.count("#")
    num_damaged_unknown = num_damaged - num_damaged_known

    unknown = [i for (i, c) in enumerate(conditions) if c == "?"]

    valid_arrangements = 0

    for damaged in combinations(unknown, num_damaged_unknown):
        if find_groups(make_arrangement(conditions, damaged)) == groups:
            valid_arrangements += 1

    return valid_arrangements


def make_arrangement(conditions, damaged):
    arrangement = list(conditions)
    for i in damaged:
        arrangement[i] = "#"
    return "".join(arrangement)


def find_groups(arrangement):
    groups = re.findall("#+", arrangement)
    return tuple(len(group) for group in groups)


def part_2_answer(lines, unfold):
    records = [parse(line) for line in lines]
    return sum(memoization_arrangements(record, unfold) for record in records)


def memoization_arrangements(record, unfold):
    conditions, groups = record

    if unfold:
        conditions = "?".join([conditions] * 5)
        groups = groups * 5

    return _memoization_arrangements(conditions, groups)


@cache
def _memoization_arrangements(conditions, groups):
    # pylint: disable=too-many-return-statements

    # Based on https://www.reddit.com/r/adventofcode/comments/18ghux0/comment/kd0npmi/

    if conditions == "":
        # No more condition characters left
        # Arrangement is valid if there are no more groups
        return 1 if (len(groups) == 0) else 0

    if conditions.startswith("."):
        # Ignore dot; consider the rest of the string
        return _memoization_arrangements(conditions[1:], groups)

    if conditions.startswith("?"):
        # Try replacing ? with both . and #
        return sum(_memoization_arrangements(c + conditions[1:], groups) for c in ".#")

    if conditions.startswith("#"):

        # Must have at least one group for the #
        if len(groups) == 0:
            return 0

        next_group = groups[0]

        # Must have enough characters for the whole group
        if len(conditions) < next_group:
            return 0

        left, right = conditions[:next_group], conditions[next_group:]

        # . will end a group, so . cannot appear in the first part
        if "." in left:
            return 0

        if (len(right) > 0) and right.startswith("#"):
            # Group is actually longer
            return 0

        if (len(right) > 0) and right.startswith("?"):
            # To end the group, the next character must be .
            right = "." + right[1:]

        return _memoization_arrangements(right, groups[1:])

    return 0


def parse(line):
    conditions, groups = line.split(" ")
    groups = tuple(int(n) for n in groups.split(","))
    return conditions, groups
