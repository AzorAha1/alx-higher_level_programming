#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    string_f = importlib.import_module("hidden_4")
    for i in dir(string_f):
        if not i.startswith("__"):
            print("{}".format(i))
