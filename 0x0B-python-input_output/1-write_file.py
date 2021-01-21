#!/usr/bin/python3
"""File manipulation to create or write a file"""


def write_file(filename="", text=""):
    """writes text to a given file"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
