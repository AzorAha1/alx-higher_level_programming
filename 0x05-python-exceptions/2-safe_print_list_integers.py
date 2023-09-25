#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    try:
        counter = 0
        onlyint = lambda x: isinstance(x, int)
        printonlyint = list(filter(onlyint, mylist))
        for c in printonlyint:
            counter+=1
        if x > counter:
            raise IndexError("list index out of range")
        [print(i, end='') for i in printonlyint[:x]]
        print()
        return x
    except Exception as e:
        print(e)