#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return(0, None)
    else:
        output = (length, sentence[0])
        return output
