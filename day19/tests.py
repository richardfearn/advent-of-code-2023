import unittest

import day19
import utils

PART_1_EXAMPLE = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""


class Part1Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(19114, day19.part_1_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(362930, day19.part_1_answer(utils.read_input_lines(19)))


class Part2Tests(unittest.TestCase):

    def test_example(self):
        self.assertEqual(167409079868000, day19.part_2_answer(utils.to_lines(PART_1_EXAMPLE)))

    def test_with_input(self):
        self.assertEqual(116365820987729, day19.part_2_answer(utils.read_input_lines(19)))
