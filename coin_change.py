def c_change(n,m,s):
    if n == 0:
        return 1
    if n < 0:
        return 0
        
    if m <= 0:
        return 0
        
    return c_change(n-s[m-1],m,s) + c_change(n,m-1,s)
    
def c_change_dp(n,m,s):
    table = [[0 for x in range(m)] for x in range(n+1)]
    
    for i in range(m):
        table[0][i] = 1
        
    for i in range(1, n+1):
        for j in range(m):
            x = table[i-s[j]][j] if i-s[j] >= 0 else 0
            y = table[i][j-1] if j > 0 else 0
            table[i][j] = x+y
        
    for i in table:
        print(i)
    
    return table[-1][-1]
    
s = [2,3,5,6]
n = 10

print(c_change_dp(n,len(s),s))
