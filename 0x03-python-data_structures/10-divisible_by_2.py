#!/usr/bin/python3
def divisible_by_2(mylist=[]):
    if len(mylist) == 0:
        return
    for item in mylist:
        if item % 2 == 0:
            return True
        else:
            return False
