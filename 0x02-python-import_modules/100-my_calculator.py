#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    wrongoperator = "Unknown operator. Available operators: +, -, * and /"
    morethan3 = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    multiplicationsign = "*"

    if len(args) != 4:
        print("{}".format(morethan3))
        exit(1)
    else:
        a = args[1]
        b = args[3]
        operator = args[2]
    if operator == "+":
        print("{} + {} = {}".format(a, b, add(int(a), int(b))))
        exit(0)
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
        exit(0)
    elif operator == "/":
        print("{} / {} = {}".format(a, b, div(int(a), int(b))))
        exit(0)
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
        exit(0)
    else:
        print("{}".format(wrongoperator))
        exit(1)
