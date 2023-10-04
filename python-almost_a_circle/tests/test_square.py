#!/usr/bin/python3

import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_area(self):
        s2 = Square(3)
        self.assertEqual(s2.area(), 9)

    def test_display(self):
        s3 = Square(2)
        expected_output = "##\n##\n"
        self.assertEqual(s3.display(), expected_output)

    def test_update(self):
        s4 = Square(1)
        s4.update(2)
        self.assertEqual(s4.id, 2)
        s4.update(2, 3, 4)
        self.assertEqual(s4.size, 3)
        self.assertEqual(s4.x, 4)
        s4.update(y=5, x=6)
        self.assertEqual(s4.x, 6)
        self.assertEqual(s4.y, 5)

    def test_to_dictionary(self):
        s5 = Square(3)
        expected_dict = {'id': 1, 'size': 3, 'x':
