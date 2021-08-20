#!/usr/bin/python3
"""peak module"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (Int): List of unsorted  integers.
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
