'''
Problem 6.2 discussed on pg. 177 of Algorithms
(Sanjoy, Christos, Umesh)
'''

from math import pow

def min_penalty_trip(A: list, n: int):
    
    i = 0
    min_sum = 0
    
    H = [] # Holds the hotels and their respective mile marker
    H.append(0) # Base case where penalty is zero for day 0

    while (i <= n):
        if (i == n):
            # We must stop at n
            min_sum += pow((200 - A[i]), 2)
        else:
            curr = abs(200 - (A[i] - H[-1]))
            for j in range(i, n):
                if abs(200 - (A[j] - H[-1])) > curr:
                    min_sum += pow((200 - A[j - 1]), 2)
                    H.append(A[j - 1])
                    i = j
                    break
                else:
                    curr = abs(200 - (A[j] - H[-1]))
                    j += 1

    return min_sum    