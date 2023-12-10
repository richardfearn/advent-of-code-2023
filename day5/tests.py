import unittest

import day5
import utils

PART_1_EXAMPLE = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(35, day5.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(309796150, day5.part_1_answer(utils.read_input_lines(5)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(46, day5.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(50716416, day5.part_2_answer(utils.read_input_lines(5)))
