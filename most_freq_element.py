arr = list(map(int, input("Enter the array - ").strip(" ").split(" ")))

fm = dict()

for i in arr:
    if i in fm.keys():
        fm[i] = fm[i] + 1
    else:
        fm[i] = 1
        
freq = 0
fi = None
for i in fm.keys():
    if freq < fm[i]:
        fi = i
        freq = fm[i]
        
print(fi)
