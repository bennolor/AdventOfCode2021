import unittest

from day6 import solution1, solution2


class TestAoC(unittest.TestCase):
    test_input = '3,4,3,1,2'

    def test_part_1(self):
        """
        Testing Part 1 of AoC Day 6 Challenge by using the given example
        :return
        """
        self.assertEqual(5934, solution1(self.test_input))

    def test_part_2(self):
        """
        Testing Part 1 of AoC Day 6 Challenge by using the given example
        :return:
        """
        self.assertEqual(26984457539, solution2(self.test_input))
