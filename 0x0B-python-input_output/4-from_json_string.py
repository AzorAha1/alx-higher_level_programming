#!/usr/bin/python3
"""function
"""
import json


def from_json_string(my_str):
    """from_json_string
    returns object represented in json(data structure)
    """
    return json.loads(my_str)
