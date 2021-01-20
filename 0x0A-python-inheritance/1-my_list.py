#!/usr/bin/python3


class MyList(list):
    """
    This class imitates the operation of a list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        ----------
        Returns
        ----------
        Sorted list
        """
        print(sorted(self))
