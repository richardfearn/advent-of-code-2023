import unittest

import day7
import utils

PART_1_EXAMPLE = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(6440, day7.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(248422077, day7.part_1_answer(utils.read_input_lines(7)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(5905, day7.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(249817836, day7.part_2_answer(utils.read_input_lines(7)))
