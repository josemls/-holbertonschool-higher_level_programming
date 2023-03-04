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
