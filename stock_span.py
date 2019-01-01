from stack import Stack

# ~ [100, 80, 60, 70, 60, 75, 85]

def span(values):
    s = Stack()
    res = [0]*len(values)
    
    s.push(0)
    res[0] = 1
    
    for i in range(1, len(values)):
        if values[i] < values[i-1]:
            res[i] = 1
        else:
            top = s.peek()
            if values[top] < values[i]:
                print('i ', i)
                print('top ', top)
                res[i] = res[top] + i - top
            else:
                res[i] = 2
            s.push(i)
    print (s.arr)
    return res
    
values = [100, 80, 60, 70, 60, 75, 85]
# ~ values = [10, 4, 5, 90, 120, 80]
print(span(values))
