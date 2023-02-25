#!/usr/bin/python3
""" Json func"""
import json


def from_json_string(my_str):
    """ Return an object representing by json string"""
    return json.loads(my_str)
