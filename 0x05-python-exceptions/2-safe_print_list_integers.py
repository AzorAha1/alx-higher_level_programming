#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    try:
        onlyint = lambda x: isinstance(x, int)
        printonlyint = list(filter(onlyint, mylist))
        [print(i, end='') for i in printonlyint[:x]]
        print()
        return x
    except IndexError as e:
        print(e)