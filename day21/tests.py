import unittest

import day21
import utils

PART_1_EXAMPLE = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(16, day21.part_1_answer(utils.to_lines(PART_1_EXAMPLE), 6))

    def test_with_input(self):
        self.assertEqual(3722, day21.part_1_answer(utils.read_input_lines(21), 64))


class Part2Tests(unittest.TestCase):

    def test_with_input(self):
        self.assertEqual(614864614526014, day21.part_2_answer(utils.read_input_lines(21), 26501365))
