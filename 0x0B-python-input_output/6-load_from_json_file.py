#!/usr/bin/python3
"""function
"""
import json


def load_from_json_file(filename):
    """load_from_json_file
    """
    with open(file=filename, mode='r') as thefile:
        theobj = json.loads(thefile.read())
        return theobj
