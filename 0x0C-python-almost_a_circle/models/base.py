#!/usr/bin/python3
""" Defines a Base class """

import json


class Base:
    """ Represents base class 
    Attributes:
        __nb_objects (int): number of instances
    """
    __nb_objects = 0
    
    def __init__(self, id = None):
        """ Base constructor
        Args:
            id (int): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string
        Args:
            list_dictionaries (list): list to convert to json
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_of_obj_dict = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_of_obj_dict))
