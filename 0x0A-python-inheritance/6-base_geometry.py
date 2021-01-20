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
