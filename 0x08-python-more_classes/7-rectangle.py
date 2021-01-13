#!/usr/bin/python3
""" Rectangle Class that defines a rectangle"""


class Rectangle:
    """
    defines a rectangle object

    Attributes:
    width (int): the width of a rectangle
    height (int): the height of a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor to inicializate the attributes of the object"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Constructor “official” string representation of an object """
        str_print = ""
        if self.__width == 0 or self.__height == 0:
            return str_print
        else:
            for row in range(self.__height):
                str_print += str(self.print_symbol) * self.__width
                if row < (self.__height - 1):
                    str_print += "\n"
            return str_print

    def __repr__(self):
        """Constructor “official” string representation of an object """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """contructor to delate a instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
