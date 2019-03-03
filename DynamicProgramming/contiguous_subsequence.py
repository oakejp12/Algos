
def max_sum_of_sequence(A: list):

    if (len(A) == 0):
        print("The provided argument list is empty.") 
        return []
    
    max_sum = 0
    max_index = 0
    current_sum = 0

    L = []
    
    for idx, i in enumerate(A):
        if i + current_sum > 0:
            L.append(i + current_sum)
            current_sum = current_sum + i
            if (current_sum > max_sum):
                max_index = idx
                max_sum = current_sum
        else:
            L.append(0)
            current_sum = 0

    print("The array of maximal sums: " + str(L))
    print("The max index: " + str(max_index))

    start_index = max_index
    current_value = L[start_index]
    S = []
    while current_value > 0:
        S.append(A[start_index])
        start_index = start_index - 1
        current_value = L[start_index]
    
    S.reverse()
    print("The contiguous subsequence: " + str(S))

    return S