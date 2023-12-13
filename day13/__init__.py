import utils

ASH, ROCK = ".", "#"


def part_1_answer(lines):
    patterns = utils.group_lines(lines)
    return sum(part_1_summary(pattern) for pattern in patterns)


def part_1_summary(pattern):
    return next(summaries(pattern))


def summaries(pattern):
    for y in find_reflections(pattern):
        yield 100 * y

    # Transpose the pattern
    pattern = list(zip(*pattern))

    for x in find_reflections(pattern):
        yield x


def find_reflections(pattern):
    for i in range(1, len(pattern)):
        num_common_lines = min(i, len(pattern) - i)
        top = pattern[i - num_common_lines:i]
        top.reverse()
        bottom = pattern[i:i + num_common_lines]
        if top == bottom:
            yield i


def part_2_answer(lines):
    patterns = utils.group_lines(lines)
    return sum(part_2_summary(pattern) for pattern in patterns)


def part_2_summary(pattern):
    prev_summary = part_1_summary(pattern)
    return next(s for s in part_2_summaries(pattern) if s != prev_summary)


def part_2_summaries(pattern):
    width, height = len(pattern[0]), len(pattern)
    pattern = [list(row) for row in pattern]
    for x in range(width):
        for y in range(height):
            old_symbol = pattern[y][x]
            pattern[y][x] = ASH if (old_symbol == ROCK) else ROCK
            yield from summaries(pattern)
            pattern[y][x] = old_symbol
