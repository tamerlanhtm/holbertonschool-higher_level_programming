#!/usr/bin/python3
"""This class contains class named BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class.

    Attributes
    ----------
        __width : int
        __height : int
    Methods
    -------
        area():
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        This function calculates the area of the rectangle
        Return
        ------
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
