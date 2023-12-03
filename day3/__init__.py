import math
import re

NUMBER_REGEX = r"\d+"


def extend(lines):
    lines = ["." + line + "." for line in lines]
    extra_row = "." * len(lines[0])
    lines = [extra_row] + lines + [extra_row]
    return lines


def part_1_answer(lines):
    lines = extend(lines)
    return sum(numbers_adjacent_to_symbol(lines))


def numbers_adjacent_to_symbol(lines):
    numbers = []
    for y, line in enumerate(lines):
        for m in re.finditer(NUMBER_REGEX, line):
            number = int(m.group(0))
            start, end = m.span(0)
            if is_adjacent_to_symbol(lines, y, start, end):
                numbers.append(number)
    return numbers


def is_adjacent_to_symbol(lines, y, start, end):
    above = lines[y - 1][start - 1:end + 1]
    below = lines[y + 1][start - 1:end + 1]
    left = lines[y][start - 1]
    right = lines[y][end]
    adjacent = set(above) | set(below) | set(left) | set(right)
    return len(adjacent) > 1


def part_2_answer(lines):
    lines = extend(lines)
    return sum(find_gear_ratios(lines))


def find_gear_ratios(lines):
    numbers = find_numbers(lines)
    ratios = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "*":
                adjacent_numbers = find_adjacent_numbers(lines, x, y, numbers)
                if len(adjacent_numbers) == 2:
                    ratios.append(math.prod(adjacent_numbers))
    return ratios


def find_numbers(lines):
    numbers = []
    for y, line in enumerate(lines):
        for m in re.finditer(NUMBER_REGEX, line):
            number = int(m.group(0))
            start, end = m.span(0)
            numbers.append((number, range(start, end), y))
    return numbers


def find_adjacent_numbers(lines, x, y, numbers):
    adjacent = set()
    for offset in (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1):
        ax, ay = x + offset[0], y + offset[1]
        if lines[ay][ax].isdigit():
            adjacent.update(num for (num, nx, ny) in numbers if (ax in nx) and (ay == ny))
    return adjacent
