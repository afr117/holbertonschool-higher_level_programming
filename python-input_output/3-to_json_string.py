#!/usr/bin/python3
"""
Module for converting objects to JSON strings.
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    if isinstance(my_obj, dict):
        my_obj = [(str(key), value) for key, value in sorted(my_obj.items())]

    return json.dumps(my_obj, ensure_ascii=False)

if __name__ == "__main__":
    to_json_string()

