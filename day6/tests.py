import unittest

import day6
import utils

PART_1_EXAMPLE = """
Time:      7  15   30
Distance:  9  40  200
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(288, day6.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(211904, day6.part_1_answer(utils.read_input_lines(6)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(71503, day6.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(43364472, day6.part_2_answer(utils.read_input_lines(6)))
