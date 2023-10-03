#!/usr/bin/python3
# retuning tuples and string length
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
