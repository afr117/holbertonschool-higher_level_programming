#!/usr/bin/python3
"""
Script to add command-line arguments to a Python list and save it to a JSON file.
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Name of the JSON file
filename = "add_item.json"

# Initialize an empty list or load from existing JSON file
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)

