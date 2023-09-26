#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        newlist = []
        for i in range(len(my_list_1)):
            result = my_list_1[i] / my_list_2[i]
            newlist.append(result)
        list_length = len(newlist)
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return newlist
    
        
            