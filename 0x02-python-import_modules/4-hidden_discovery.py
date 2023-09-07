#!/usr/bin/python3

import hidden_4 as hidden
for i in dir(hidden):
      if not i.startswith("__"):
        print("{}".format(i))
