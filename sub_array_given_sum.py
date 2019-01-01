def subarray_sum(A, target):
    sum_so_far = 0
    for i in range(len(A)):
        sum_so_far = 0
        for j in range(i, len(A)):
            sum_so_far += A[j]
            if sum_so_far > target:
                break
            if sum_so_far == target:
                return (i,j)
    return ()

def subarray_sum_optimised(A, target):
    sum_so_far = 0
    j = 0
    for i in range(len(A)):
        sum_so_far += A[i]
        while sum_so_far > target and j < i:
            sum_so_far -= A[j]
            j += 1
        if sum_so_far == target:
            return (j,i)
    return -1

# ~ A = [1, 4, 20, 3, 10, 5]
# ~ target = 0
# ~ print(subarray_sum_optimised(A, target))
t = int(input())
while t > 0:
    t-=1
    n,s = list(map(int,input().strip().split(" ")))
    A = list(map(int,input().strip().split(" ")))
    ans = subarray_sum_optimised(A,s)
    if ans == -1:
        print(ans)
    else:
        j, i = ans
        print("{} {}".format(j+1,i+1))
