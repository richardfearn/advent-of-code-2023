import unittest

import day12
import utils

PART_1_EXAMPLE = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(21, day12.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(7633, day12.part_1_answer(utils.read_input_lines(12)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        for (unfold, answer) in (False, 21), (True, 525152):
            with self.subTest(unfold=unfold, answer=answer):
                self.assertEqual(answer, day12.part_2_answer(utils.to_lines(PART_1_EXAMPLE), unfold))

    def test_with_input(self):
        for (unfold, answer) in (False, 7633), (True, 23903579139437):
            with self.subTest(unfold=unfold, answer=answer):
                self.assertEqual(answer, day12.part_2_answer(utils.read_input_lines(12), unfold))
