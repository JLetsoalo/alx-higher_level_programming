#!/usr/bin/python3
# 100-safe_print_integer_err.py

from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        stderr.write("Exception: {}\n".format(e))
        return (False)
