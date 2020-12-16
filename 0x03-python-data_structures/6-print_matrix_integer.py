#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        spac = ""
        for column in row:
            print("{:s}{:d}".format(spac, column), end="")
            spac = " "
        print()
