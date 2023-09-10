#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return(0, None)
    output = (len(sentence), sentence[0])
    if not output:
        return None
    return output
