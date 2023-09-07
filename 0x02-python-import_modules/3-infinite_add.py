#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    args = sys.argv
    if len(args) == 1:
        print("0")
    else:
        args = sys.argv[1:]
        for i in args:
            sum += int(i)
        print(sum)
