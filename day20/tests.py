import unittest

import day20
import utils

PART_1_EXAMPLE_1 = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

PART_1_EXAMPLE_2 = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(32000000, day20.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1)))

    def test_example_2(self):
        self.assertEqual(11687500, day20.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2)))

    def test_with_input(self):
        self.assertEqual(896998430, day20.part_1_answer(utils.read_input_lines(20)))


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        self.assertEqual(236095992539963, day20.part_2_answer(utils.read_input_lines(20)))
