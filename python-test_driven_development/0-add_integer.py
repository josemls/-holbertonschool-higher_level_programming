#!/usr/bin/python3
""" Function that adds two integers """


def add_integer(a, b=98):
        """ Definition of function that return te addition of two integers
        Args:
                a (int or float): argument one
                b (int or float): argument two
        Raises:
                TypeError: if 'a' or 'b' are not int or float
        Returns:
                the two parameters add result
        """
        if type(a) is not int and type(a) is not float:
                raise TypeError("a must be an integer")
        if type(b) is not int and type(b) is not float:
                raise TypeError("b must be an integer")
        return int(a) + int(b)
