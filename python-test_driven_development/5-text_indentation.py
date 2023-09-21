#!/usr/bin/python3
"""
This module provides various functions for performing calculations.
You can use these functions to add, subtract, multiply, and divide numbers. 
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""
    add_newline = False

    for char in text:
        new_text += char
        if char in chars:
            new_text += '\n\n'
            add_newline = True
        else:
            add_newline = False

    lines = new_text.split('\n')
    formatted_lines = [line.strip() for line in lines if line.strip()]
    formatted_text = '\n'.join(formatted_lines)

    print(formatted_text)

