#!/usr/bin/python3
"""
inheriting from the base geometry tasks
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        integer validation
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height