#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Initialize private attribute
        Args:
        size(int) = is the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """Getter"""
    @property
    def position(self):
        return self.position

    """ prints in stdout the square with the character #"""

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            for row in range(self.__position[1]):
                print()

            for i in range(self.__size):
                if self.__position[0] != 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)

    """Setter"""
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
