#!/usr/bin/python3
"""This module defines Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    Attributes
    ----------
        __size : int
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, width=self.__size, height=self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
