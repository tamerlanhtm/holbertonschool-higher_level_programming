#!/usr/bin/python3
"""This module contains write_file() function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written
    Parameters
    ----------
        filename : str
        text : str
    """
    with open(filename, mode="w", encoding="UTF-8") as file:
        number_of_characters = file.write(text)
    return number_of_characters
