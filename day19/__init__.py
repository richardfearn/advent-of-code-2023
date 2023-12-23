import math
import operator
import re
from collections import deque

import utils

OPERATORS = {
    "<": operator.lt,
    ">": operator.gt,
}

IN_WORKFLOW = "in"

ACCEPTED, REJECTED = "A", "R"

EMPTY_RANGE = range(0, 0)


def part_1_answer(lines):
    workflows, ratings = parse(lines)
    return sum(sum(rating.values()) for rating in ratings if accepted(rating, workflows))


def accepted(rating, workflows):
    current = (IN_WORKFLOW, 0)

    while current not in {ACCEPTED, REJECTED}:

        current_workflow, current_rule_num = current
        rule = workflows[current_workflow][current_rule_num]

        if isinstance(rule, str):
            current = rule

        else:
            category, op, value, destination = rule

            if op(rating[category], value):
                current = destination
            else:
                current = (current_workflow, current_rule_num + 1)

        if isinstance(current, str) and (current not in {ACCEPTED, REJECTED}):
            current = (current, 0)

    return current == ACCEPTED


def part_2_answer(lines):
    workflows, _ = parse(lines)

    start = ({category: range(1, 4001) for category in "xmas"}, (IN_WORKFLOW, 0))

    to_explore = deque()
    to_explore.append(start)

    total_accepted = 0

    while len(to_explore) > 0:

        current = to_explore.popleft()
        current_ranges, (current_workflow, current_rule_num) = current

        if current_workflow == ACCEPTED:
            total_accepted += math.prod(len(n) for n in current_ranges.values())

        elif current_workflow == REJECTED:
            pass

        else:
            rule = workflows[current_workflow][current_rule_num]

            if isinstance(rule, str):
                new_state = (current_ranges, (rule, 0))
                to_explore.append(new_state)

            else:
                split(current_ranges, current_workflow, current_rule_num, rule, to_explore)

    return total_accepted


def split(current_ranges, current_workflow, current_rule_num, rule, to_explore):
    # pylint: disable=too-many-locals

    category, op, value, destination = rule

    rule_if_true = (destination, 0)
    rule_if_false = (current_workflow, current_rule_num + 1)

    if op == operator.gt:
        value += 1
        rule_if_true, rule_if_false = rule_if_false, rule_if_true

    range_left, range_right = split_range(current_ranges[category], value)

    for (range_part, next_rule) in ((range_left, rule_if_true), (range_right, rule_if_false)):
        if len(range_part) > 0:
            new_state = (make_new_ranges(current_ranges, category, range_part), next_rule)
            to_explore.append(new_state)


def make_new_ranges(current_ranges, category, new_range):
    new_ranges = current_ranges.copy()
    new_ranges[category] = new_range
    return new_ranges


def split_range(r, i):
    if i <= r.start:
        return EMPTY_RANGE, r

    if r.stop < i:
        return r, EMPTY_RANGE

    return range(r.start, i), range(i, r.stop)


def parse(lines):
    workflows, ratings, *_ = utils.group_lines(lines)[0:2]
    workflows = dict(parse_workflow(line) for line in workflows)
    ratings = [parse_rating(line) for line in ratings]
    return workflows, ratings


def parse_workflow(line):
    workflow_name, rules = line.split("{")
    rules = rules[:-1]
    rules = rules.split(",")
    rules[:-1] = [parse_rule(rule) for rule in rules[:-1]]
    return workflow_name, rules


def parse_rule(r):
    m = re.match(r"([xmas])([<>])(\d+):(A|R|[a-z]+)", r)
    return m.group(1), OPERATORS[m.group(2)], int(m.group(3)), m.group(4)


def parse_rating(line):
    values = line[1:-1].split(",")
    values = [value.split("=") for value in values]
    values = {category: int(rating) for category, rating in values}
    return values
