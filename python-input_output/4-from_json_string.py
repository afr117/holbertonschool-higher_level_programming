#!/usr/bin/python3
"""
Module for converting JSON strings to Python objects.
"""

import json

def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str: The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)

if __name__ == "__main__":
    from_json_string()
