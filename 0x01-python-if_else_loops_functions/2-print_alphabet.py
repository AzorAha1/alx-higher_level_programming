#!/usr/bin/python3
for string in range(97, 123):
    alpha = chr(string)
    print(alpha.format(alpha), end='')
