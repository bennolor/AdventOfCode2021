import unittest

from day6 import solution1

class TestAoC(unittest.TestCase):
    def test_part_1(self):
        """
        Testing Part 1 of AoC
        :return
        """
        self.assertEqual(5934, solution1('3,4,3,1,2'))