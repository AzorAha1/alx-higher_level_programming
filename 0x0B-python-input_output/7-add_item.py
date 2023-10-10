#!/usr/bin/python3
"""function
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
with open(file=filename, mode='w') as thefile:
    save_to_json_file(sys.argv[1:], filename)
