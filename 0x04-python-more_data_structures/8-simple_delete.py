#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    check_exist = key in a_dictionary
    if check_exist is True:
        del a_dictionary[key]
    return a_dictionary
