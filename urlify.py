def urlify(arr, l):
    i = 0
    while i < l:
        if arr[i] == " ":
            arr[i] = '%'
            j = l-1
            while j >= i+1:
                arr[j+2] = arr[j]
                j -= 1
            arr[i+1] = '2'
            arr[i+2] = '0'
            l = l+2
        i += 1
    return arr

arr = ['m','r',' ','j','o','h','n',' ','s','m','i','t','h','','','','',]
print(''.join(urlify(arr,13)))
