import unittest

import day14
import utils

PART_1_EXAMPLE = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(136, day14.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(109665, day14.part_1_answer(utils.read_input_lines(14)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(64, day14.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(96061, day14.part_2_answer(utils.read_input_lines(14)))
