def check_permutation(s1, s2):
    
    if len(s1) != len(s2):
        return False
    '''
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    '''
    fm = {}
    for i in s1:
        if i in fm.keys():
            fm[i] += 1
        else:
            fm[i] = 1
    
    for i in s2:
        if i in fm.keys():
            fm[i] -= 1
        else:
            return False
        if fm[i] == 0:
            del fm[i]
    
    if len(fm) == 0:
        return True
    else:
        return False
    
    
s1 = "afbdgc"
s2 = "fgcabd"
print(check_permutation(s1,s2))
