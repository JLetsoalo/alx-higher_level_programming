#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """Intiates new Rectangle.

        Argsuments:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns: area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() & str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
