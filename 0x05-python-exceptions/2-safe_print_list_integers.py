#!/usr/bin/python3
#safe printing list of int

def safe_print_list_integers(my_list=[], x=0):
    outted = 0
    for indx in range(x):
        try:
            print("{:d}".format(my_list[indx]), end="")
        outted += 1
        except (TypeError, ValueError):
            continue
    print("")
    return outted
