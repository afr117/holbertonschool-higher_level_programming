#!/usr/bin/python3
"""Module that defines the MyList class."""


class MyList(list):
    """A class that inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
