#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    string = dir(importlib.import_module("hidden_4"))
    for i in string:
        if not i.startswith("__"):
            print("{}".format(i))
