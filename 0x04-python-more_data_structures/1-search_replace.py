#!/usr/bin/python3
def search_replace(mylist, search, replace):
    mylist = list(map(lambda x : x if x != search else replace, mylist))
    return mylist