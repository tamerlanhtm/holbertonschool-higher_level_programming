#!/usr/bin/python3
"""This module contains the is_same_class() function."""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of the given class.

    Parameters:
        obj : object
            The object to check.
        a_class : class
            The class to compare against.

    Returns:
        bool:
            True if obj is an instance of a_class.
            False if obj is not an instance of a_class or
            if a_class is the object class.
    """
    if type(obj) is a_class:
        return True
    return False
