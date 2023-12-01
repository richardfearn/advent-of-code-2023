import unittest

import day1
import utils

PART_1_EXAMPLE = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

PART_2_EXAMPLE = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(142, day1.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(55488, day1.part_1_answer(utils.read_input_lines(1)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(281, day1.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(55614, day1.part_2_answer(utils.read_input_lines(1)))
