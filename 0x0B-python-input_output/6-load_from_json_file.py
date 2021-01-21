#!/usr/bin/python3
"""This reads a file and store it's object"""
import json


def load_from_json_file(filename):
    """Reads a json file and recovers the object """
    with open(filename) as my_file:
        return (json.loads(my_file.read()))
