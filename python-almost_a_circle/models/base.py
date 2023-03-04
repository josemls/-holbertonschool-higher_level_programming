#!/usr/bin/python3
""" class base"""
import json
import csv
import os.path


class Base:
        """ class called Base"""
        __nb_objects = 0

        def __init__(self, id=None):
                """ initializer method"""
                if id is not None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = self.__nb_objects
        
        @staticmethod
        def to_json_string(list_dictionaries):
                """Return JSON string """
                if list_dictionaries is None:
                        return "[]"
                return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
                """Writes the JSON string representation """
                filename = "{}.json".format(cls.__name__)
                list_dic = []

                if list_objs is None:
                        pass
                else:
                        for i in range(len(list_objs)):
                                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as file:
            file.write(lists)