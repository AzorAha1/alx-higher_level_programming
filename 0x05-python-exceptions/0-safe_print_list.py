#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    try:
        counter = 0
        for c in mylist:
            counter += 1
        if x > counter:
            x = counter
        [print(i, end='') for i in mylist[:x]]
        print()
        return x
    except Exception as e:
        print("error:", e)
