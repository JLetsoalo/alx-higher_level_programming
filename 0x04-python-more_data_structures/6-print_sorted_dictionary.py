#!/usr/bin/python3
# 6-print_sorted_dictionary.py


def print_sorted_dictionary(a_dictionary):
    [print("{}: {}".format(b, a_dictionary[b])) for b in sorted(a_dictionary)]
