import unittest

import day22
import utils

PART_1_EXAMPLE = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(5, day22.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(512, day22.part_1_answer(utils.read_input_lines(22)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(7, day22.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(98167, day22.part_2_answer(utils.read_input_lines(22)))
