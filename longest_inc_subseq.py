import sys
def lis(A,prev,curr):
    if curr == len(A):
        return 0
        
    taken = 0
    if A[curr] > prev:
        taken = 1 + lis(A, A[curr], curr+1)
    
    nottaken = lis(A,prev, curr+1)
    
    return max(taken, nottaken)

A = [10,9,2,5,3,7,101,18]
prev = -sys.maxsize + 1
curr = 0
print(lis(A,prev,curr))
