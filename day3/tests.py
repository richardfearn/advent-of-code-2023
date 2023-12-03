import unittest

import day3
import utils

PART_1_EXAMPLE = """
467..114..
...*......
. 35 .633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(4361, day3.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(512794, day3.part_1_answer(utils.read_input_lines(3)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(467835, day3.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(67779080, day3.part_2_answer(utils.read_input_lines(3)))
