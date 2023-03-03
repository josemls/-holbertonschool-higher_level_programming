#!/usr/bin/python3

"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y