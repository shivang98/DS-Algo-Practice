# ~ arr1 = list(map(int, input("Enter the array1 - ").strip(" ").split(" ")))
# ~ arr2 = list(map(int, input("Enter the array2 - ").strip(" ").split(" ")))

arr1 = [-1,0,1,3,4,6,7,9]
arr2 = [1,2,4,5,7,9,10]

l1 = len(arr1)
l2 = len(arr2)
i = 0
j = 0
res = []
while i<l1 and j<l2:
    if arr1[i] == arr2[j]:
        res.append(arr1[i])
        i += 1
        j += 1
    elif arr1[i] < arr2[j]:
        i += 1
    else:
        j += 1
        
print(res)
