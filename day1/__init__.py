WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
WORD_DIGITS = {word: str(i + 1) for (i, word) in enumerate(WORDS)}


def part_1_answer(lines):
    def calibration_value(line):
        digits = [c for c in line if c.isdigit()]
        return int(digits[0] + digits[-1])

    return sum(calibration_value(line) for line in lines)


def part_2_answer(lines):
    def calibration_value(line):
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for word, digit in WORD_DIGITS.items():
                if line[i:i + len(word)] == word:
                    digits.append(digit)
        return int(digits[0] + digits[-1])

    return sum(calibration_value(line) for line in lines)
