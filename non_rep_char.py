s = input()

fm = {}

for i in s:
    if i not in fm.keys():
        fm[i] = 1
    else:
        fm[i] += 1
        

for i in s:
    if fm[i] == 1:
        print(i)
        break;
        
if fm[i] != 1:
    print(None)
