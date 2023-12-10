import math
from itertools import cycle


def part_1_answer(lines):
    instructions, next_elements = parse(lines)
    return num_steps("AAA", instructions, next_elements, part_1_end)


def part_1_end(element):
    return element == "ZZZ"


def part_2_answer(lines):
    instructions, next_elements = parse(lines)
    start_elements = [e for e in next_elements.keys() if e.endswith("A")]
    steps_for_each = [num_steps(e, instructions, next_elements, part_2_end) for e in start_elements]
    return math.lcm(*steps_for_each)


def part_2_end(element):
    return element.endswith("Z")


def num_steps(start, instructions, next_elements, end_predicate):
    current = start
    steps = 0
    next_instruction_iter = cycle(instructions)

    while not end_predicate(current):
        next_instruction = next(next_instruction_iter)
        current = next_elements[current][next_instruction]
        steps += 1

    return steps


def parse(lines):
    instructions = lines[0]

    next_elements = lines[2:]
    next_elements = [s.split(" = ") for s in next_elements]
    next_elements = [(a, b[1:-1].split(", ")) for a, b in next_elements]
    next_elements = [(a, dict(zip(["L", "R"], b))) for a, b in next_elements]
    next_elements = dict(next_elements)

    return instructions, next_elements
