#!/usr/bin/python3
""" File manipulation to Python data structure represented by a JSON"""

import json


def from_json_string(my_str):
    """ Write a function that returns an object represented by a JSON """

    return json.loads(my_str)
