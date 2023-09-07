#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    for i in dir(hidden):
        if not i.startswith("__"):
            print("{}".format(i))
