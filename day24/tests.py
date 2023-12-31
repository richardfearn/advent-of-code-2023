import unittest

import day24
import utils

PART_1_EXAMPLE = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2, day24.part_1_answer(utils.to_lines(PART_1_EXAMPLE), use_example_limits=True))

    def test_with_input(self):
        self.assertEqual(20336, day24.part_1_answer(utils.read_input_lines(24), use_example_limits=False))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(47, day24.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(677656046662770, day24.part_2_answer(utils.read_input_lines(24)))
