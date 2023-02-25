#!/usr/bin/python3
""" geometry module"""


class BaseGeometry():
    """ class base geometry"""
    def area(self):
        """func that raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ func that check if value is not integer or if
        value is less or equal than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))