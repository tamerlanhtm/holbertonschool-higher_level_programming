#!/usr/bin/python3
"""This module contains the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance or
    subclass instance of the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
