#!/usr/bin/python3
"""Defines the square class size"""


class Square:
    """Has a size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be of int type")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
