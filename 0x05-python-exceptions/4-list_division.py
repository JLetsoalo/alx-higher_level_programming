#!/usr/bin/python3
#divides two lists and then
#lists types of divisions used

def list_division(my_list_1, my_list_2, list_length):
    freshList = []
    for x in range(list_length):
        div = 0
        try:
            div = my_list_1[x] / my_list_2[x]
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            freshList.append(div)
    return freshList
