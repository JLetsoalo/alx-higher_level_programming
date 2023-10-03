#!/usr/bin/python3
# 10-best_score.py


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    r_out = list(a_dictionary.keys())[0]
    big = a_dictionary[r_out]
    for g, v in a_dictionary.items():
        if v > big:
            big = v
            r_out = g
    return (r_out)
