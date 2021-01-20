#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Template for a Rectangle object
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        calculate the area of a Rectangle shape
        Return
        -------
        Area of a Rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        prints the width and height of a rectangle
        Return
        -------
        string with the class, heigh and width
        """
        return (f"Rectangle {self.__width}/{self.__height}")
