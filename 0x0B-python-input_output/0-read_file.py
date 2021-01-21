#!/usr/bin/python3
"""file manipulation using python"""


def read_file(filename=""):
    """Read file template function."""
    with open(filename, "r") as my_file:
        print(my_file.read(), end="")
    my_file.close()
