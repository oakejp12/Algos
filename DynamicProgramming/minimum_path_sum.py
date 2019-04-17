'''
Given an m * n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path
'''


def calc_min_path_sum(A: list, m: int, n: int) -> list:
    '''
    Return an array D where D[i][j] = A[i][j] + min(A[i][j-1], A[i - 1][j])
    '''

    D = [[0] * n for i in range(m)]

    for i in range(0, m):
        for j in range(0, n):
            # Calculate the min sum
            if (i - 1) < 0 and (j - 1) < 0:
                D[i][j] = A[i][j]
            elif (i - 1) < 0:
                D[i][j] = A[i][j] + D[i][j - 1]
            elif (j - 1) < 0:
                D[i][j] = A[i][j] + D[i - 1][j]
            else:
                min_sum = min(D[i - 1][j], D[i][j - 1])
                D[i][j] = A[i][j] + min_sum

    return D


def backtrack_calc_min_sum(A: list, D: list, m: int, n: int) -> int:
    '''
    Backtrack to find min path sum from bottom-right to top-left
    '''

    # Grab the most bottom-right element
    min_sum = A[m - 1][n - 1]

    # i, j are used as indices
    i = m - 1
    j = n - 1

    while (i > 0) or (j > 0):
        if (i - 1) < 0:
            min_sum = min_sum + A[i][j - 1]
            j = j - 1
        elif (j - 1) < 0:
            min_sum = min_sum + A[i - 1][j]
            i = i - 1
        else:
            if (D[i - 1][j] < D[i][j - 1]):
                min_sum = min_sum + A[i - 1][j]
                i = i - 1
            else:
                min_sum = min_sum + A[i][j - 1]
                j = j - 1

    return min_sum
