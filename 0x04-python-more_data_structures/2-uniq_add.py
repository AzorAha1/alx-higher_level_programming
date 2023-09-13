#!/usr/bin/python3
def uniq_add(mylist=[]):
    result = 0
    mylist = set(mylist)
    for i in mylist:
        result += i
    return result
