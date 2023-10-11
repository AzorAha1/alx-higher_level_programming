#!/usr/bin/python3
"""function
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
with open(file=filename, mode='r'):
    try:
        mylist = load_from_json_file(filename)
    except Exception:
        mylist = []
    mylist.extend(sys.argv[1:])
with open(file=filename, mode='w'):
    save_to_json_file(data, filename)
