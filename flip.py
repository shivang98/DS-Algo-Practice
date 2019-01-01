import sys
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A  = [int(i) for i in A]
        for i in range(len(A)):
            if A[i] == 0: A[i] = -1
            
        l = -1
        r = -1
        m = sys.maxsize
        s = 0
        x = -1
        y = -1
        flag = False
        
        for i in range(len(A)):
            s = s + A[i]
            
            if s > 0:
                s = 0
                flag = False
                
            if s < 0:
                if not flag:
                    x = i
                    y = i
                    flag = True
                y = i
            
            if s < m:
                m = s
                l = x
                r = y
                
        if l!= -1:
            return [l+1,r+1]
        else:
            return []

A = [1,1,1,0,0,1,0,0,1,1,0]
B = [1,1,1,1,1,1]
A = '11100100110'
ob = Solution()
print(ob.flip(A))
