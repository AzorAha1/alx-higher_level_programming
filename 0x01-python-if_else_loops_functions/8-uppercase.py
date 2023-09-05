#!/usr/bin/python3
def uppercase(str):
    uppercase_name = ""
    for string in str:
        upstr = ord(string)
        if 97 <= upstr <= 122:
            uppercase_name += chr(upstr - 32)
        else:
            uppercase_name += string
    print("{}".format(uppercase_name))
