import sys

def mc_change(s,n):
    if n == 0:
        return 0
    
    a = sys.maxsize
    for i in s:
        if i <= n:
            a = min(a, mc_change(s, n-i)+1)
            
    if a == sys.maxsize:
        return 0
    return a
    
def mc_change_dp(s,n):
    table = [sys.maxsize for i in range(n+1)]
    table[0] = 0

    for i in range(1,n+1):
        for j in s:
            if j <= i:
                table[i] = min(table[i],table[i-j]+1)
    if table[n] == sys.maxsize: return 0
    return table[n]

s = [2,3,5,6]
n = 10

print(mc_change_dp(s,n))
