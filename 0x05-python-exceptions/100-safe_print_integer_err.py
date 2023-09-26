#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError("Unknown format code 'd' for object of type 'str'")
    except Exception as e:
        print("{}".format(e), file=sys.stderr)
        return False
