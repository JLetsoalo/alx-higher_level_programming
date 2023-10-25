#!/usr/bin/python3
# 5-square.py
"""Define a class Square and its properties"""


class Square:
    """the square."""
    def __init__(self, size):
        """Initialize a new square.
        """
        self.size = size

    @property
    def size(self):
        """set current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be of int type")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square using the hash character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
