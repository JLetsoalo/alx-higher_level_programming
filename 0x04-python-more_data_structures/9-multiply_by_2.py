#!/usr/bin/python3
# 9-multiple_by_2.py


def multiply_by_2(a_dictionary):
    """creates new dictionary with values multipled by 2."""
    return ({b: a_dictionary[b] * 2 for b in a_dictionary})
