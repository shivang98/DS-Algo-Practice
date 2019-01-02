def palindrome_perm(S):
    S = S.lower()
    S = ''.join(S.split(' '))
    fm = {}
    for i in S:
        if i in fm.keys():
            fm[i] += 1
        else:
            fm[i] = 1
    print(fm)
    if len(S) % 2 == 0:
        for k in fm.values():
            if k % 2 != 0:
                return False
    else:
        flag = False
        for k in fm.values():
            if k %2 == 0:
                continue
            elif k %2 == 1:
                if flag:
                    return False
                else:
                    flag = True
            else:
                return False
    return True
    
S = 'Tact Coa'
print(palindrome_perm(S))
