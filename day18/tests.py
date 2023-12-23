import unittest

import day18
import utils

PART_1_EXAMPLE = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(62, day18.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(49578, day18.part_1_answer(utils.read_input_lines(18)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(952408144115, day18.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(52885384955882, day18.part_2_answer(utils.read_input_lines(18)))
