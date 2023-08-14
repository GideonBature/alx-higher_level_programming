#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers """
    for rows in matrix:
        for num in range(len(rows)):
            if num == len(rows) - 1:
                print("{:d}".format(rows[num]), end="")
            else:
                print("{:d}".format(rows[num]), end=" ")
        print()
