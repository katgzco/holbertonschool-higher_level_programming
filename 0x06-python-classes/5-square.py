#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Initialize private attribute
        Args:
        size(int) = is the size of the square
    """
    def __init__(self, size=0):
        self.__size = size

    """returns the current square area"""

    def area(self):
        return self.__size**2

    """Getter"""
    @property
    def size(self):
        return self.__size

    """Setter"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ prints in stdout the square with the character #"""

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
