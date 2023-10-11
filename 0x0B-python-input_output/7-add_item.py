#!/usr/bin/python3
"""function
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
if os.path.exists(filename):
    mylist = load_from_json_file(filename)
else:
    mylist = []
mylist.extend(sys.argv[1:])
with open(filename, 'w') as thefile:
    save_to_json_file(mylist, filename)
