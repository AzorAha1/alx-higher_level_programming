#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
lastdigit = int(num_str[-1])
string = "Last digit of"
if lastdigit > 5:
    print(f'{string} {number} is {lastdigit} and is greater than 5')
elif lastdigit == 0:
    print(f'{string} is {lastdigit}')
else:
    print(f'{string} {number} is {lastdigit} and is less than 6 and not 0')
