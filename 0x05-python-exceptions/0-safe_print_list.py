#!/usr/bin/python3
def safe_print_list(mylist=[], x = 0):
    counter = 0
    for i in mylist:
        counter+=1
    try:
        for i in mylist:
            print("{}".format(i), end="")
        print()
        return x
    except Exception:
        return Exception