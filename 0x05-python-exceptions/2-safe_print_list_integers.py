#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    try:
        counter = 0
        onlyint = lambda x: isinstance(x, int)
        printonlyint = list(filter(onlyint, mylist))
        [print("{:d}".format(i), end='') for i in printonlyint[:x]]
        print()
        return x
    except Exception as e:
        print(e)