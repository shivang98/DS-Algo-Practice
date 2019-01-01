from stack import Stack

def span(values):
    s = Stack()
    res = [0]*len(values)
    
    s.push(0)
    res[0] = 1
    
    for i in range(1, len(values)):
        while s.isEmpty()!= True and values[i] > values[s.peek()]:
            s.pop()
        if s.isEmpty():
            res[i] = i + 1
        else:
            res[i] = i - s.peek()
        s.push(i)
    return res
    
# ~ values = [100, 80, 60, 70, 60, 75, 85]
values = [10, 4, 5, 90, 120, 80]
print(span(values))
