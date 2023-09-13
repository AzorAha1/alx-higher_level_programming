#!/usr/bin/python3
def search_replace(mylist, search, replace):
    for i in range(len(mylist)):
        if mylist[i] == search:
            mylist[i] = replace
            return mylist