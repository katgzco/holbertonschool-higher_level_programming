#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map((lambda t_lis:
                list(map(lambda x: x * x, t_lis))), matrix))
