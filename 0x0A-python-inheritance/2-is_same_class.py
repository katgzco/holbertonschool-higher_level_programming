#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    check if a object is exactly an instance of the specified class
    Parameters
    ----------
    obj : is a instance of the class
    a_class : is a class
    Returns
    ----------
    True if the object is an instance of the class or False.
    """
    return (type(obj) == a_class)
