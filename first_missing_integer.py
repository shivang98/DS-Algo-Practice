class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # ~ if A == [1]:
            # ~ return 2
        A.append(0)
        curr = 0 
        pos = 0
        tmp = 0
        for i in range(len(A)):
            if A[i] < 0 or A[i] > len(A)-1 or A[i] == i:
                continue

            curr = A[i]
            pos = A[curr]
            A[curr] = curr
            
            while pos >= 0 and pos < len(A) and A[pos] != pos:
                tmp = A[pos]
                A[pos] = pos
                pos = tmp
        
        # ~ print(A)
        
        for i in range(1, len(A)):
            if A[i] != i:
                return i

        return A[-1]+1
        
A = [-1,2,5,6,-9,1,3]
# ~ A = [0,1,2,3,4,5]
# ~ A = [1,2,3,4,5]
# ~ A = [-1, -9, -2]
ob = Solution()
print(ob.firstMissingPositive(A))
