WORDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


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
            for word in WORDS:
                if line[i:i + len(word)] == word:
                    digits.append(str(WORDS.index(word) + 1))
        return int(digits[0] + digits[-1])

    return sum(calibration_value(line) for line in lines)
