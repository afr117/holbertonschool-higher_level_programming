#!/usr/bin/python3
"""
Module for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the text file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added

if __name__ == "__main__":
    append_write()
