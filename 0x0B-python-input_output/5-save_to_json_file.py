#!/usr/bin/python3
"""function
"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    write an object to a txt file using json
    """
    with open(file=filename, mode='w') as thefile:
        json_obj = json.dumps(my_obj)
        return thefile.write(json_obj)
