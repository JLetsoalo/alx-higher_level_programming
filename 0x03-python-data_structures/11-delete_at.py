#!/usr/bin/python3
# deeleting items on list

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    output = []
    for x in range(len(my_list)):
        if x != idx:
            output.append(my_list[x])

    return output
