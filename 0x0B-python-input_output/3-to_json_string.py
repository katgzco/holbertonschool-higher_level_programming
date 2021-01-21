#!/usr/bin/python3
""" File manipulation to JSON representation of an object """

import json


def to_json_string(my_obj):
    """ Function that returns the JSON representation of an object """

    return json.dumps(my_obj)
