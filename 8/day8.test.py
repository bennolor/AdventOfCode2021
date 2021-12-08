import unittest
from day8 import solution1, solution2

class TestAoC(unittest.TestCase):
    test_input = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

    def test_part_1(self):
        """
        Testing Day 8 Part one
        :return:
        """
        self.assertEqual(26,solution1(self.test_input))
