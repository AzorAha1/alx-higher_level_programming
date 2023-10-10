#!/usr/bin/python3
import json
def load_from_json_file(filename):
    with open(file=filename, mode='r') as thefile:

        return json.loads(thefile.read())