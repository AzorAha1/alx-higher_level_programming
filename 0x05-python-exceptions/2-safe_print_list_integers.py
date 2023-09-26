#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    try:
        def onlyint(x):
            return isinstance(x, int)
        counter = 0
        printonlyint = list(filter(onlyint, mylist))
        [print("{:d}".format(i), end='') for i in printonlyint[:x]]
        print()
        return x
    except Exception as e:
        print(e)
