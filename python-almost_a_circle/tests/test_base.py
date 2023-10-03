#!/usr/bin/python3

import unittest
from base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(98)
        self.assertEqual(b2.id, 98)

        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        # Add test cases for to_json_string method
        pass

    def test_save_to_file(self):
        # Add test cases for save_to_file method
        pass

    def test_from_json_string(self):
        # Add test cases for from_json_string method
        pass

    def test_create(self):
        # Add test cases for create method
        pass

    def test_load_from_file(self):
        # Add test cases for load_from_file method
        pass

if __name__ == "__main__":
    unittest.main()
