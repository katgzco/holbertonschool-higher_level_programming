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
            raise TypeError("width must be >= 0")
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
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Methods - returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Method - returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
