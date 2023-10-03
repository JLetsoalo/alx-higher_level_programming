#!/usr/bin/python3

def uniq_add(my_list=[]):
    output = 0
    for y in set(my_list):
        output += y
    return (output)
