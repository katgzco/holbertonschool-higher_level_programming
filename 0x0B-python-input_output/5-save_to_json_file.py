#!/usr/bin/python3
"""saves an obj in json format"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object in json representation. """
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(my_obj))
    json_file.close()
