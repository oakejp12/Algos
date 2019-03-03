'''
Minimizing Chain matrix Multiplication
'''

from sys import maxsize
from pandas import DataFrame as df


def chain_matrix_multiply(M: list, n: int):
    '''
    M: a list of matrix sizes to multiply
    n: the number of matrices to multiply
    '''

    # Initialize a n*n matrix to all zeros
    # Create a list of n elements, each of which a list of n zeros
    C = [[0] * n for i in range(n)]

    print(df(C))

    for s in range(1, n):
        print("S: " + str(s))
        for i in range(1, n - s):
            j = i + s  # Iterate to the next column
            print("i: " + str(i))
            print("s: " + str(s))
            print("j: " + str(j))
            print(df(C))
            for l in range(i, j - 1):
                print("Testing all the possibilities of l: " + str(l))
                curr = (M[i - 1] * M[l] * M[j]) + (C[i][l] + C[l + 1][j])
                print("Current: " + str(curr))
                if (C[i][j] == 0):
                    C[i][j] = curr
                elif (C[i][j] > curr):
                    C[i][j] = curr

    print(df(C))
    print("Final solution: " + str(C[0][n - 1]))

    return C[0][n - 1]
