#!/usr/bin/python3

import unittest
import json
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
        b1 = Base(1)
        b2 = Base(2)
        json_str = Base.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        self.assertEqual(json_str, '[{"id": 1}, {"id": 2}]')

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [{"id": 1}, {"id": 2}])

    def test_from_json_string(self):
        json_str = '[{"id": 1}, {"id": 2}]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(obj_list, [{"id": 1}, {"id": 2}])

    def test_create(self):
        obj_dict = {"id": 3}
        obj = Base.create(**obj_dict)
        self.assertEqual(obj.id, 3)

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        obj_list = Base.load_from_file()
        self.assertEqual(obj_list, [b1, b2])

if __name__ == "__main__":
    unittest.main()
