def count_ways(n, S):
    if n == 0:
        return 1
    if n < 0:
        return 0
    ans = 0
    for i in S:
        ans += count_ways(n-i,S)
        
    return ans
    
def count_ways_dp(n, S, M):
    if n == 0:
        return 1
    if n < 0:
        return 0
    ans = 0
    
    if M[n] > -1:
        return M[n]
    
    for i in S:
        M[n-i] = count_ways(n-i,S)
        ans += M[n-i]
        
    return ans
    

    
    
n = 4
S = [1,2,3]
print(count_ways_dp(n, S,[-1]*5))
