#!/usr/bin/python3
"""This module defines a class named Square."""


class Square:
    """
    Defines a square.

    Attributes
    ----------
        size : int
            The size of the square's side.
    Methods
    -------
        area():
            Returns the area of the square.
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns
        -------
            __size : int
                Size attribute of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square.
        Parameters
        ----------
            size : int
                The new size of the square's side.
        Raises
        ------
            TypeError
                If size is not an integer.
            ValueError
                If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.
        Returns
        -------
            __size**2 : int
                The area of the square.
        """
        return self.__size**2
