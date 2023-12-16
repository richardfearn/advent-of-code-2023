import unittest

import day16
import utils

PART_1_EXAMPLE = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(46, day16.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(7477, day16.part_1_answer(utils.read_input_lines(16)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(51, day16.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(7853, day16.part_2_answer(utils.read_input_lines(16)))
