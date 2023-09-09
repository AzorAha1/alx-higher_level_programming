#!/usr/bin/python3
def no_c(my_string):
    newstring = my_string.translate( {ord(n):None for n in 'Cc'} )
    return newstring
