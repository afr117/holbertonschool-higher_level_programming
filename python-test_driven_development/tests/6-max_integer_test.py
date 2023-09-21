#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_mixed_list(self):
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([99]), 99)

    def test_float_list(self):
        self.assertEqual(max_integer([1.5, 3.7, 2.2, 0.9]), 3.7)

if __name__ == '__main__':
    unittest.main()

