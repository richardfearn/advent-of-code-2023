import unittest

import day11
import utils

PART_1_EXAMPLE = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(374, day11.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(9742154, day11.part_1_answer(utils.read_input_lines(11)))


class Part2Tests(unittest.TestCase):

    def test_example_scale_10(self):
        self.assertEqual(1030, day11.part_2_answer(utils.to_lines(PART_1_EXAMPLE), 10))

    def test_example_scale_100(self):
        self.assertEqual(8410, day11.part_2_answer(utils.to_lines(PART_1_EXAMPLE), 100))

    def test_with_input(self):
        self.assertEqual(411142919886, day11.part_2_answer(utils.read_input_lines(11)))
