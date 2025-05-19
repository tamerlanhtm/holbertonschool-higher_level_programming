#!/usr/bin/python3
"""This module defines a class named Square."""


class Square:
    """
    Defines a square.

    Attributes
    ----------
        __size : int
            The size of the square's side.
        __position : tuple
            position of the square
    Methods
    -------
        area():
            Returns the area of the square.
        my_print():
            Print the square with the character '#'.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.
        Returns
        -------
            __position : tuple
                The position attribute of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position attribute of the square.
        Parameters
        ----------
            value : tuple
                Tuple containing the coordinates of the square (x, y).
        Raises
        ------
            TypeError
                If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        Returns
        -------
            __size**2 : int
                The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Print the square with the character '#'.
        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for height in range(self.__size):
            print(" " * self.__position[0], end="")
            for width in range(self.__size):
                print("#", end="")
            print()
