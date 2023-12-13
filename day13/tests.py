import unittest

import day13
import utils

PART_1_EXAMPLE = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(405, day13.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(27664, day13.part_1_answer(utils.read_input_lines(13)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(400, day13.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(33991, day13.part_2_answer(utils.read_input_lines(13)))
