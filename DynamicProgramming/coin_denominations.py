'''
Problem 6.17 - Algorithms [DPV]:
Given an unlimited supply of coins of denominations, x1, ..., xn
is it possible to make change for a value (v
'''


def is_change_possible(A: list, V: int):
    '''
    Create a 1-Dim. array C to hold values of A
    possible to use when making change for V
    If C[V] == V, then change is possible
    '''

    C = []
    C.append(0)

    for v in range(1, V):
        C.append(0)  # Take care of intializating C[v]
        for i in range(len(A)):  # Try out all possible coins
            if (C[v] == V):
                return True  # If we already have our answer, return early

            current_val = A[i]
            if (current_val <= v and C[v] < current_val + C[v - 1] and C[v - 1] + current_val <= V):
                C[v] = current_val + C[v - 1]

    return C[-1] == V
