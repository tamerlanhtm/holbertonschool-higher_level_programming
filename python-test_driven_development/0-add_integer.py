#!/usr/bin/python3

"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    This function adds two integers.

    Args:
        a: Integer or float. If float, it will be cast to an integer.
        b: Integer or float. If float, it will be cast to an integer.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.

    Returns:
        The sum of the integers or floats, both cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
