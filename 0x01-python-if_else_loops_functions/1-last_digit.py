#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
string = "Last digit of"
longstr = "and is less than 6 and not 0"
if lastdigit < 6 and lastdigit != 0:
    if number < 0:
        print(f'{string} {number} is -{lastdigit} {longstr}')
elif lastdigit > 5:
    print(f'{string} {number} is {lastdigit} and is greater than 5')
elif lastdigit == 0:
    print(f'{string} {number } is {lastdigit} and is {lastdigit}')
else:
    print("Error")
