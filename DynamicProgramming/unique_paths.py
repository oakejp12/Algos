'''
A robot is located at the top-left corner of a m * n grid
The robot can only move either down or right at any point in time
The robot is trying to reach the bottom-right corner of the grid
How many possible unique paths are there?
'''


def unique_paths(m: int, n: int) -> int:

    if (m == 0 and n == 0):
        return 0

    # Initialize bottom-up array
    # to 1 since there's at least
    # 1 unique path from start to end
    D = [[1] * m for i in range(n)]

    # For some reason this problem is formulated
    # such that m = columns and n = rows --> stupid.
    # so fix indices
    for i in range(1, n):
        for j in range(1, m):
            # Take the number of unique paths
            # from D[i][j - 1] and the number of
            # unqiue paths from D[i - 1][j] and add them 
            D[i][j] = D[i][j - 1] + D[i - 1][j]

    return D[-1][-1]


if __name__ == "__main__":

    m = 3
    n = 2
    output = 3

    assert(unique_paths(m, n) == output)

    m = 7
    n = 3
    output = 28
    assert(unique_paths(m, n) == output)
