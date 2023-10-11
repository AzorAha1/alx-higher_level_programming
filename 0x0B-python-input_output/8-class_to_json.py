#!/usr/bin/python3
"""function
"""
json = __import__('json')


def class_to_json(obj):
    """class_to_json
    """
    jsoninstr = json.dumps(obj=obj.__dict__)
    return json.loads((jsoninstr))
