#!/usr/bin/python3


def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    gigi = 0

    for c in range(len(roman_string)):
        if roman_dict.get(roman_string[c], 0) == 0:
            return (0)

        if (c != (len(roman_string) - 1) and
                roman_dict[roman_string[c]] < roman_dict[roman_string[c + 1]]):
                digi += roman_dict[roman_string[c]] * -1

        else:
            digi += roman_dict[roman_string[c]]
    return (digi)
