#!/usr/bin/python3
""" Defines unittest for max_integer([...]) """


import unittest
max_integer = __import__("6-max_integer").max_integer
class Test_max_integer(unittest.TestCase):
    """ unittest for max_integer """

    def test_max_at_end(self):
        matrix = [1,2,3,4]
        self.assertEqual(max_integer(matrix), 4)
    def test_max_at_beggining(self):
        matrix = [4,3,2,1]
        self.assertEqual(max_integer(matrix), 4)

    def test_max_in_middle(self):
        matrix = [1,3,2]
        self.assertEqual(max_integer(matrix), 3)

    def test_one_neg(self):
        matrix = [-1, 0, 1]
        self.assertEqual(max_integer(matrix), 1)

    def test_multiple_neg(self):
        matrix = [-3,-2,-1]
        self.assertEqual(max_integer(matrix), -1)

    def test_one_arg(self):
        matrix = [9]
        self.assertEqual(max_integer(matrix), 9)

    def test_empty_list(self):
        matrix = []
        self.assertEqual(max_integer(matrix), None)

if __name__ == "__main__":
    unittest.main()
