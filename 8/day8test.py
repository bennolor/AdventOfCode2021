import unittest
from day8 import solution1, solution2


class TestAoC(unittest.TestCase):
    with open('testin.txt', 'r') as test_input_file:
        test_input = test_input_file.readlines()

    def test_part_1(self):
        """
        Testing Day 8 Part one
        :return:
        """
        self.assertEqual(26, solution1(self.test_input))
