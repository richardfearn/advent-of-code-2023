import unittest

import day17
import utils

PART_1_EXAMPLE = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

PART_2_EXAMPLE = """
111111111111
999999999991
999999999991
999999999991
999999999991
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(102, day17.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(942, day17.part_1_answer(utils.read_input_lines(17)))


class Part2Tests(unittest.TestCase):

    def test_part_1_example(self):
        self.assertEqual(94, day17.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_part_2_example(self):
        self.assertEqual(71, day17.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(1082, day17.part_2_answer(utils.read_input_lines(17)))
