#!/usr/bin/python3
def safe_print_division(a, b):
    global result
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("{}".format(result))
        return result
