import unittest

import day9
import utils

PART_1_EXAMPLE = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(114, day9.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1861775706, day9.part_1_answer(utils.read_input_lines(9)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2, day9.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1082, day9.part_2_answer(utils.read_input_lines(9)))
