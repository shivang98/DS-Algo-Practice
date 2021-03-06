#code
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
    
t = int(input())
while t > 0:
    t-=1
    n = int(input())
    A = list(map(int,input().split(" ")))
    print(equilibrium_optimised(A))
