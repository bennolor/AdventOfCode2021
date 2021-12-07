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

    def test_part2(self):
        """
        Testing Part 2 of AoC Day 7
        :return:
        """
        self.assertEqual(168, solution2(self.test_input))

        with open('in.txt','r') as in_file:
            line = in_file.readline()
        self.assertEqual(104822130, solution2(line))