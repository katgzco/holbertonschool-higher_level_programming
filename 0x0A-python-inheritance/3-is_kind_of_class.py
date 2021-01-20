#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    check if the object is an instance of a class that inherited from a class
    Parameters
    ----------
    obj : is a instance of the class
    a_class : is a class
    Returns
    ----------
    True if the object is an instance of the class or False.
    """
    return isinstance(obj, a_class)
