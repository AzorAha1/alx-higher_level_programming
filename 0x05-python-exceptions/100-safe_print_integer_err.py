#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except Exception as e:
        print(e, file=sys.stderr)