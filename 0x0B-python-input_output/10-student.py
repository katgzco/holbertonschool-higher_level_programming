#!/usr/bin/python3
""" Define a class Student that defines a studen """


class Student:
    """ This template represents a student """
    def __init__(self, first_name, last_name, age):
        """Constructor for students"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict of students"""
        if attrs is None:
            return self.__dict__
        if all(isinstance(at, str) for at in attrs):
            if isinstance(attrs, list):
                return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
