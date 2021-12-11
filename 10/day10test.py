import unittest
try:
    from day10 import solution1, solution2
except ImportError:
    pass


class TestAoC(unittest.TestCase):
    with open("testin.txt", "r") as input_file:
        test_input = input_file.readlines()

    def test_solution1(self):
        self.assertEqual(26397, solution1(self.test_input))

    def test_solution2(self):
        self.assertEqual(288957, solution2(self.test_input))
