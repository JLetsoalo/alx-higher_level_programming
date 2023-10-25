#!/usr/bin/python3
#safe printing integer

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False  
