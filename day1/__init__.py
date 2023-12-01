import re

WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

REGEX = f"(?=({'|'.join(WORDS)}|[1-9]))"

VALUES = {word: i + 1 for (i, word) in enumerate(WORDS)} | {str(i): i for i in range(1, 10)}


def part_1_answer(lines):
    def calibration_value(line):
        digits = [c for c in line if c.isdigit()]
        return int(digits[0] + digits[-1])

    return sum(calibration_value(line) for line in lines)


def part_2_answer(lines):
    def calibration_value(line):
        digits = re.findall(REGEX, line)
        first, last = digits[0], digits[-1]
        return VALUES[first] * 10 + VALUES[last]

    return sum(calibration_value(line) for line in lines)
