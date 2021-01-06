#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Initialize private attribute
        Args:
        size(int) = is the size of the square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """returns the current square area"""

    def area(self):
        return self.__size**2
