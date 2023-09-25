#!/usr/bin/python3
def safe_print_list(mylist=[], x = 0):
    try:
        counter = 0
        if not mylist:
            return 0
        for i in mylist:
            counter+=1
        if x > counter:
            x = counter
        [print(i, end='')for i in mylist[:x]]
        print()
        return x
    except Exception as ex:
        print("error:", ex)     
