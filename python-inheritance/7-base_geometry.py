#!/usr/bin/python3
"""This class contains class named BaseGeometry"""


class BaseGeometry:
    """
       BaseGeometry class

       Method
       ------
            area():
            integer_validator():
    """
    def area(self):
        """
        Area method

        Raise
        -----
            Exception:
                area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates the value

        Parameters
        ----------
            name : str
            value : int
        Raise
        -----
             TypeError
                If the value is not an integer
            ValueError
                If the value is less than or equal to 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
