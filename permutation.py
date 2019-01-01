def permutation(s):
    
    if len(s) == 1:
        base = []
        base.append(s)
        return base
    
    ch = s[0]
    ros = s[1:]
    
    small_ans = permutation(ros)
    
    ans = []
    for i in small_ans:
        for idx in range(len(i)+1):
            tmp = i[:idx] + ch + i[idx:]
            ans.append(tmp)
    return ans

s = 'abcc'
print (permutation(s))
