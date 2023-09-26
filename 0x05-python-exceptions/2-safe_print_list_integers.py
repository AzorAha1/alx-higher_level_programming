#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
    try:
        def onlyint(x):
            return isinstance(x, int)
        counter = 0
        printonlyint = list(filter(onlyint, mylist))
        for c in printonlyint:
            counter += 1
        if x >= counter:
            x = counter
        [print("{:d}".format(i), end='') for i in printonlyint[:x]]
        print()
        return x
    except IndexError as e:
        print("Error")
