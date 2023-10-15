#!/usr/bin/python3
"""class
"""
import json


class Base:
    """Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            jrep = json.dumps(list_dictionaries)
            return jrep

    @classmethod
    def save_to_file(cls, list_objs):
        list_objs_list = []
        with open(file="{}.json".format(cls.__name__), mode='w') as fp:
            for obj in list_objs:
                list_objs_list.append(obj.to_dictionary())
            fp.write(cls.to_json_string(list_dictionaries=list_objs_list))
