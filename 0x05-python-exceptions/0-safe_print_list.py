#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indx = 0
    while indx < x:
        try:
            print("{}".format(my_list[indx]), end="")
        except IndexError:
            break
        indx += 1
    print("")
    return indx
