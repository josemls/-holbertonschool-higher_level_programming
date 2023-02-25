#!/usr/bin/python3
"""Checks if an object is inherited"""


def inherits_from(obj, a_class):
    """Checking if the object is an instance of the class."""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)