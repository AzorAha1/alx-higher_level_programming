#!/usr/bin/python3
"""class
"""
import json
import os
import csv


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
        """save to file
        listobj
        """
        list_objs_list = []
        if list_objs is None:
            list_objs = []
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
        """create
        create
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        # here you create the file name with json extension
        filename = cls.__name__ + ".json"
        # create an empty list for instances
        listofinstances = []
        # if file doesnt exist return empty list
        if not os.path.exists(filename):
            return listofinstances
        else:
            # now read from the file
            with open(file=filename, mode='r') as f:
                # now read the file and store in variable data
                data = f.read()
                # now convert data to list of json str rep
                datalist = cls.from_json_string(data)
                # iterate through every data in datalist set attributes
                for onedata in datalist:
                    instance = cls.create(**onedata)
                    listofinstances.append(instance)
        return listofinstances

    @classmethod
    def save_to_file_csv(cls, list_obj):
        list_obj_list = []
        filename = cls.__name__ + ".csv"
        if list_obj is None:
            list_obj = []
        else:
            with open(file=filename, mode='w') as thefile:
                if cls.__name__ == 'Rectangle':
                    csvformat = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == 'Square':
                    csvformat = ["id", "size", "x", "y"]
                writer = csv.DictWriter(thefile, fieldnames=csvformat)
                listofdicts = [obj.to_dictionary() for obj in list_obj]
                writer.writeheader()
                writer.writerows(listofdicts)

    @classmethod
    def load_from_file_csv(cls):
        list_ofinstances = []
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return list_ofinstances
        else:
            with open(file=filename, mode='r') as file:
                reader = csv.DictReader(file)
                for read in reader:
                    instance = cls.create(**read)
                    list_ofinstances.append(instance)
        return list_ofinstances
