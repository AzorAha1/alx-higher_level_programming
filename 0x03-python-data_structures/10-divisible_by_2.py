#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    newlist = []
    for item in mylist:
        if int(item) % 2 == 0:
            return newlist.append(True)
        else:
            return newlist.append(False)
    return newlist