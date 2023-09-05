#!/usr/bin/python3
for number in range(0, 99):
    if number == 98: 
        print("{:02}".format(number))
    else:
        print("{:02}".format(number), end=', ', flush=True)
