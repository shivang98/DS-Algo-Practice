import sys

def maxConti(arr):
    m = -(sys.maxsize-1)
    s = 0
    for i in arr:
        s += i
        if s < 0:
            s = 0
        if s > m:
            m = s
    return m


t = int(input())
while t > 0:
    t -= 1
    n,k = list(map(int,input().split(" ")))
    A = list(map(int,input().split(" ")))
    
    s = 0
    p = False
    neg = False
    for i in A:
        if i < 0:
            p = True
            break
        else:
            s += i
    
    mi = -sys.maxsize + 1
    for i in A:
        if i > 0:
            neg = True
            break
        else:
            if mi < i:
                mi = i
        
    if p == False:
        print (s * k)
        continue
        
    if neg == False:
        print(mi)
        continue
    
    B = []
    for i in range(k):
        B.extend(A)
        
    print(maxConti(B))

