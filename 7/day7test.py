import unittest
from day7 import solution1,solution2

class TestAoC(unittest.TestCase):
    test_input = '16,1,2,0,4,2,7,1,2,14'

    def test_part1(self):
        """
        Testing Part 1 of AoC Day 7
        :return:
        """
        self.assertEqual(37, solution1(self.test_input))
