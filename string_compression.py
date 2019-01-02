def compress(S):
    res = ['']
    count = 1
    
    for i in range(len(S)-1):
        if res[-1] != S[i]:
            res.append(S[i])
        if S[i] == S[i+1]:
            count += 1
        else:
            if count > 1: res.append(str(count))
            count = 1
    
    if res[-1] != S[-1]: res.append(S[-1])
    if count > 1: res.append(str(count))
    res = ''.join(res)
    if len(S) > len(res):
        return res
    else:
        return S
        
S = "abbbc"
print(compress(S))
