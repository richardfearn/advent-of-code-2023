import unittest

import day8
import utils

PART_1_EXAMPLE_1 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

PART_1_EXAMPLE_2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

PART_2_EXAMPLE = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(2, day8.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(6, day8.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_with_input(self):
        self.assertEqual(14681, day8.part_1_answer(utils.read_input_lines(8)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(6, day8.part_2_answer(utils.to_lines(PART_2_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(14321394058031, day8.part_2_answer(utils.read_input_lines(8)))
