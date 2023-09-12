#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    newlist = []
    for item in mylist:
        if item % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist
