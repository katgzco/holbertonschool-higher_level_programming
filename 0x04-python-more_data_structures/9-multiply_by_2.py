#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_di = {}
    for key in a_dictionary:
        new_di[key] = a_dictionary[key] * 2
    return new_di
