def equilibrium(A):
    for i in range(len(A)):
        sl = 0
        for il in range(i):
            sl += A[il]
        for ir in range(i+1, len(A)):
            sl -= A[ir]
        if sl == 0:
            return i
    return -1
    
def equilibrium_optimised(A):
    if len(A)==1:
        return 1
    left_sum = 0
    right_sum = sum(A[1:])
    idx = 1
    while idx < len(A):
        left_sum += A[idx-1]
        right_sum -= A[idx]
        if left_sum == right_sum:
            return idx+1
        idx += 1
    return -1
    
A = []
print(equilibrium_optimised(A))
