#!/usr/bin/python3

"""This module defines a function `print_square` that prints a square."""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for height in range(size):
        [print("#", end="") for width in range(size)]
        print()
