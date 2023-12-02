import unittest

import day2
import utils

PART_1_EXAMPLE = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(8, day2.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(2685, day2.part_1_answer(utils.read_input_lines(2)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(2286, day2.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(83707, day2.part_2_answer(utils.read_input_lines(2)))
