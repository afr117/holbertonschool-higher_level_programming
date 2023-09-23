#!/usr/bin/python3
"""
1-my_list
"""


class MyList(list):
    """
    A class that inherits from list and provides additional methods.
    """

    def print_sorted(self):
        """
        Print the list, but sorted in ascending order.
        """
        print(sorted(self))
