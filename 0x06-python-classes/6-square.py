#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Initialize private attribute
        Args:
        size(int) = is the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    """Getter"""
    @property
    def position(self):
        return self.__position

    """Setter"""
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
                value[0] < 0 or value[1] < 0 or \
                type(value[1]) is not int or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """returns the current square area"""

    def area(self):
        return self.__size**2

    """ prints in stdout the square with the character #"""

    def my_print(self):

        if self.__size == 0 and self.__position[1] == 0:
            print()
        elif self.__position[1] != 0:
            print()

        for i in range(self.__size):
            if self.__position[0] != 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)
