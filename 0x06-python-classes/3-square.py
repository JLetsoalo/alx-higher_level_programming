#!/usr/bin/python3
"""
Square with private attribute size and public attribute area
"""


class Square:
    """
    class Square definition
    """

    def __init__(self, size=0):
        """
        Initializes square
        """
        if type(size) is not int:
            raise TypeError("size must be of int type")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size)**2
