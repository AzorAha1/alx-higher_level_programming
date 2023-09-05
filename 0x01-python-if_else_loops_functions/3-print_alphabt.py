#!/usr/bin/python3
for string in range(97, 123):
    alpha = chr(string)
    if alpha != 'q' and alpha != 'e':
        print(alpha.format(alpha), end='')
