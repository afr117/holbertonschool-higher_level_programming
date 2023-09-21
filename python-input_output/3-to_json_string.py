#!/usr/bin/python3
"""
Module for converting objects to JSON strings.
"""

import json
from collections import OrderedDict

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    class OrderedEncoder(json.JSONEncoder):
        def encode(self, obj):
            return super().encode(obj)

    ordered_obj = json.loads(json.dumps(my_obj, ensure_ascii=False), object_pairs_hook=OrderedDict)
    return json.dumps(ordered_obj, ensure_ascii=False, cls=OrderedEncoder)

if __name__ == "__main__":
    to_json_string()
