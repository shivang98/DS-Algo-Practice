def edit(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    # replace
    if len(s1) == len(s2):
        i = 0
        j = 0
        miss = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                miss += 1
            if miss > 1:
                return False
            i += 1
        return True
    
    # insert and remove
    else:
        sm,lg = (s1, s2) if len(s1) < len(s2) else (s2, s1)
        i = 0
        j = 0
        miss = 0
        while i < len(lg) and j < len(sm):
            if lg[i] != sm[j]:
                i += 1
                miss += 1
            if miss > 1:
                return False
            i += 1
            j += 1
        return True

s1 = 'pales'
s2 = 'pale'
print(edit(s1,s2))
