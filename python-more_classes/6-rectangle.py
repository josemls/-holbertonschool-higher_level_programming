#!/usr/bin/python3
""" Module with a Rectangle class"""


class Rectangle():
        """ class initialization"""

        number_of_instances = 0

        def __init__(self, width=0, height=0):
                """ function that defines the variables"""
                self.width = width
                self.height = height
                Rectangle.number_of_instances += 1

        @property
        def width(self):
                """ Function that get the width
                Return:
                        private attribute width
                """
                return self.__width

        @property
        def height(self):
                """ Function that get the height
                Return:
                        private attribute height
                """
                return self.__height

        @width.setter
        def width(self, value):
                """ Function that set the value of width
                Args:
                        value (int): width
                Raises:
                        TypeError: if value is not int
                        ValueError: if value is less than 0
                """
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value < 0:
                        raise ValueError("width must be >= 0")
                self.__width = value

        @height.setter
        def height(self, value):
                """ Function that set the value of height
                Args:
                        value (int): height
                Raises:
                        TypeError: if value is not int
                        ValueError: if value is less than 0
                """
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                if value < 0:
                        raise ValueError("height must be >= 0")
                self.__height = value

        def area(self):
                """ Function that return the area
                Return: area of rectangle
                """
                return self.__height * self.__width

        def perimeter(self):
                """ function that return the perimeter
                Return: perimeter of rectangle
                """
                if self.__width == 0 or self.__height == 0:
                        return 0
                return self.__height*2 + self.__width*2

        def __str__(self):
                """ function that return string representation"""
                if self.__width == 0 or self.__height == 0:
                        return ""
                p = "#" * self.__width
                for i in range(self.__height - 1):
                        p += "\n"
                        p += "#" * self.__width
                return p

        def __repr__(self):
                """ string representation"""
                w = self.__width
                return "Rectangle({:d}, {:d})".format(w, self.__height)

        def __del__(self):
                """ delete function"""
                print("Bye rectangle...")
                Rectangle.number_of_instances -= 1
