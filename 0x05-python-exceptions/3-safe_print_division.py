#!/usr/bin/python3
def safe_print_division(a, b):
    global result
    try:
        result = a / b
    except ZeroDivisionError:
        print("None")
    finally:
        print("{:d}".format(result))
