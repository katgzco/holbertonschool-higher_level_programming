#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry():
    """
    Template for a base geometry
    """

    def area(self):
        """
        raises an Exception
        """
        if self:
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates if value is integer
        Parameters
        ----------
        name : is a variable for store the value
        value : is the value to validate
    """
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
