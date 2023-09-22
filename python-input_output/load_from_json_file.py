#!/usr/bin/python3
"""
Module for loading Python objects from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename: The name of the JSON file to load.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
