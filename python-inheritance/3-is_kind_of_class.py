#!/usr/bin/python3
""" is kind of class fun"""


def is_kind_of_class(obj, a_class):
    """ function that return True if object is
    an instance of the specified class
    or if the object is an instance of a class that inherited
    from, otherwise False
    """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    return False