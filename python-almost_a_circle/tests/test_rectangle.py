#!/usr/bin/python3

import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_area(self):
        r2 = Rectangle(3, 7)
        self.assertEqual(r2.area(), 21)

    def test_display(self):
        r3 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        self.assertEqual(r3.display(), expected_output)

    def test_update(self):
        r4 = Rectangle(1, 1)
        r4.update(2)
        self.assertEqual(r4.id, 2)
        r4.update(2, 3, 4)
        self.assertEqual(r4.width, 3)
        self.assertEqual(r4.height, 4)
        r4.update(y=5, x=6)
        self.assertEqual(r4.x, 6)
        self.assertEqual(r4.y, 5)

    def test_to_dictionary(self):
        r5 = Rectangle(3, 4)
        expected_dict = {'id': 1, 'width': 3, 'height': 4, 'x': 0, 'y': 0}
        self.assertEqual(r5.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
