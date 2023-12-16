import unittest

import day15
import utils

PART_1_EXAMPLE = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


class Part1Tests(unittest.TestCase):

    def test_calculate_hash(self):
        self.assertEqual(52, day15.calculate_hash("HASH"))

    def test_example(self):
        self.assertEqual(1320, day15.part_1_answer(PART_1_EXAMPLE.strip()))

    def test_with_input(self):
        self.assertEqual(520500, day15.part_1_answer(utils.read_input(15)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(145, day15.part_2_answer(PART_1_EXAMPLE.strip()))

    def test_with_input(self):
        self.assertEqual(213097, day15.part_2_answer(utils.read_input(15)))
