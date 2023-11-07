#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains method inherits_from
returns True if obj is instance of class that it inherits from or is subcls of
"""


def inherits_from(obj, a_class):
    """
    Notes:
    type() - to get specific class
    obj - isinstance() to get class and any parent classes too
    a-class - issubclass() to get what object is a subclass of

    Returns:
        True - if obj is instance of class that it inherits from or is subcls of
        Otherwise - False
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
