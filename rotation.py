A = [1,2,3,4,5,6,7]
B = [4,5,6,7,5,2,3]

if len(A) == len(B):
    i = 0
    j = 0
    
    while j < len(B) and B[j] != A[0]:
        j += 1
        
    while i < len(A):
        
        if j >= len(B):
            j = 0

        if A[i] == B[j]:
            i += 1
            j += 1
        else:
            print("False")
            break
    if i == len(A): print("True")
else:
    print("False")
