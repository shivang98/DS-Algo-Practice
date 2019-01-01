s1 = 'abse'
s2 = 'abe'

l1 = len(s1)
l2 = len(s2)


if abs(l1 - l2) > 1:
    print (False)
    exit()

if abs(l1-l2) == 1:
    if l1>l2:
        small = s2
        large = s1
    else:
        small = s1
        large = s2
        
    miss = 0
    i = 0
    j = 0
    while i<len(small) and j<len(large):
        if small[i] == large[j]:
            i+=1
            j+=1
        else:
            miss += 1
            j+=1
        
        if miss > 1:
            break
    
    if miss > 1:
        print("False")
    else: print(True)
    
elif l1==l2:
    miss = 0
    i = 0
    j = 0
    while i<l1 and j<l2:
        if s1[i] != s2[j]:
            miss += 1
        i+=1
        j+=1
        if miss > 1:
            break    
        
    if miss > 1:
        print("False")
    else: print (True)
