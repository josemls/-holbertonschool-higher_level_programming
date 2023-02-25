#!/usr/bin/python3
""" Json func"""
import json


def load_from_json_file(filename):
    """ read an json file"""
    with open(filename, 'r') as f:
        x = json.load(f)
    return