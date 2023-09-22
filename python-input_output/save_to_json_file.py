#!/usr/bin/python3
"""
Module for saving Python objects to a JSON file.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file in JSON representation.

    Args:
        my_obj: The Python object to save.
        filename: The name of the file to write the JSON representation to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False)
