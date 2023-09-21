#!/usr/bin/python3
"""
This module provides various functions for performing calculations.
You can use these functions to add, subtract, multiply, and divide numbers. 
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Hello. How are you?")
        Hello.
        How are you?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = [".", "?", ":"]
    lines = []

    line = ""
    for char in text:
        line += char
        if char in separators:
            lines.append(line.strip())
            line = ""

    if line:
        lines.append(line.strip())

    for line in lines:
        print(line)
