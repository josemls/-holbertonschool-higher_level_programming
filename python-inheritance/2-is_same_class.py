#!/usr/bin/python3
"""
prints the elements of the list
"""


def is_same_class(obj, a_class):
    """ Checking if the object is the
        same class as the class
    """
    if type(obj) is a_class:
        return (True)

    else:
        return (False)