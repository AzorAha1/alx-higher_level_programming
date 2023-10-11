#!/usr/bin/python3
"""function
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
with open(file=filename, mode='w') as thefile:
    try:
        data = load_from_json_file(filename)
    except:
        data = []
    data.extend(sys.argv[1:])
    save_to_json_file(data, filename)
