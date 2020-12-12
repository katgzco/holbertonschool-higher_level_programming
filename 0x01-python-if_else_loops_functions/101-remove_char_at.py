#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    if (n >= 0 and n <= len(str)):
        new_string += str[:n]
        new_string += str[n + 1:]
    else:
        new_string = str
    return new_string
