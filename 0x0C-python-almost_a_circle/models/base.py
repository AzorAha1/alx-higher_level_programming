#!/usr/bin/python3
"""class
"""
import json
import os


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
        """to json string"""
        if list_dictionaries is None:
            return "[]"
        else:
            jrep = json.dumps(list_dictionaries)
            return jrep

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        list_objs_list = []
        with open(file="{}.json".format(cls.__name__), mode='w') as fp:
            for obj in list_objs:
                list_objs_list.append(obj.to_dictionary())
            fp.write(cls.to_json_string(list_dictionaries=list_objs_list))

    def from_json_string(json_string):
        """from json string"""
        if json_string is None:
            return []
        else:
            rep = json.loads(json_string)
        return rep

    @classmethod
    def create(cls, **dictionary):
        """create"""
        dummy = cls(1, 2, 3, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        else:
            cls.from_json_string(filename)
            return cls.create()
