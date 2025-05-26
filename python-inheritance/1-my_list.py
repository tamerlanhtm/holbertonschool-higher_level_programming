#!/usr/bin/python3
"""This module contains the MyList class that inherits from the list class."""


class MyList(list):
    """
    This class inherits from the list class.

    Methods
    -------
    print_sorted():
        Prints the list in ascending order.
    """
    def print_sorted(self):
        """Returns a new list in ascending order."""
        print(sorted(self))
        return sorted(self)
