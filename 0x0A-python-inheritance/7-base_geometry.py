#!/usr/bin/python3
"""
Module: 7-base_geometry

Contains BaseGeometry
with public instance method area and integer_validation
"""


class BaseGeometry:
    """
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks input
        Args:
            name (str): always a string
            value (int): always greater than 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
