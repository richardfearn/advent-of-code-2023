import unittest

import day10
import utils

PART_1_EXAMPLE_1 = """
.....
.S-7.
.|.|.
.L-J.
.....
"""

PART_1_EXAMPLE_2 = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

PART_2_EXAMPLE_1 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

PART_2_EXAMPLE_3 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

PART_2_EXAMPLE_4 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


class Part1Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(4, day10.part_1_answer(utils.to_lines(PART_1_EXAMPLE_1), "F"))

    def test_example_2(self):
        self.assertEqual(8, day10.part_1_answer(utils.to_lines(PART_1_EXAMPLE_2), "F"))

    def test_with_input(self):
        self.assertEqual(6714, day10.part_1_answer(utils.read_input_lines(10), "|"))


class Part2Tests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(4, day10.part_2_answer(utils.to_lines(PART_2_EXAMPLE_1), "F"))

    def test_example_3(self):
        self.assertEqual(8, day10.part_2_answer(utils.to_lines(PART_2_EXAMPLE_3), "F"))

    def test_example_4(self):
        self.assertEqual(10, day10.part_2_answer(utils.to_lines(PART_2_EXAMPLE_4), "7"))

    def test_with_input(self):
        self.assertEqual(429, day10.part_2_answer(utils.read_input_lines(10), "|"))
