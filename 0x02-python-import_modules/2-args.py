#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    args = sys.argv
    if len(args) == 1:
        args = sys.argv[0]
        print("0 arguments.")
    elif len(args) > 1:
        args = sys.argv[1:]
        if len(args) == 1:
            print("{} argument:".format(len(args)))
        else:
            print("{} arguments:".format(len(args)))
        for argument in args:
            counter += 1
            print("{}: {}".format(counter, argument))
