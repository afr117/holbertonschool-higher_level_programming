#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Use the pop() method to delete the key if it exists
    a_dictionary.pop(key, None)
    return a_dictionary
