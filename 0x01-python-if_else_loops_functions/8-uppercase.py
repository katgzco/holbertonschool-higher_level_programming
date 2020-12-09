#!/usr/bin/python3
def uppercase(str):
    """Return True if the letter is lowercase or False."""
    for char in str:
        if (ord(char) >= 97 and ord(char) <= 123):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
