#!/usr/bin/python3
""" Rectangle Class that defines a rectangle"""


class Rectangle:
    """
    defines a rectangle object

    Attributes:
    width (int): the width of a rectangle
    height (int): the height of a rectangle
    """

    def __init__(self, width=0, height=0):
        """ Constructor to inicializate the attributes of the object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
