#!/usr/bin/python3
def delete_at(mylist=[], idx=0):
    if len(mylist) == 0 or idx < 0:
        return mylist
    del mylist[idx]
    return mylist
