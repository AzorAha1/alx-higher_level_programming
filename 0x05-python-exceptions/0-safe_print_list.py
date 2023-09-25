#!/usr/bin/python3
def safe_print_list(mylist=[], x = 0):
    try: 
        [print(i, end='')for i in mylist[:x]]
        print()
        return x
    except:
        print("error")     
