#!/usr/bin/python3
# 8-rectangle.py
"""Defines a class Rectangle - inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Starts a new Rectangle.

        Argsuments:
            width (int): width of the Rectangle.
            height (int): height of Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
