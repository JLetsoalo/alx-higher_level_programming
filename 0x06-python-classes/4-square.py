#!/usr/bin/python3
"""Defines the square class with properties"""


class Square:
    """Square Has a size"""
    def __init__(self, size=0):
        """Square iniialisation"""
        if type(size) is not int:
            raise TypeError("size must be of int type")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """outputs area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """outputs size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square"""
        if type(value) is not int:
            raise TypeError("size must be of int type")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
