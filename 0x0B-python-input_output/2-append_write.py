#!/usr/bin/python3
""" File manipulation to appends a string at the end of a text  """


def append_write(filename="", text=""):
    """ Function to append a text in a file """

    with open(filename, 'a') as f:
        return f.write(text)
