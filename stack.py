class Stack:
    def __init__(self):
        self.top = -1
        self.arr = []
        
    def push(self, val):
        self.arr.append(val)
        self.top += 1
        
    def pop(self):
        res = self.arr.pop(-1)
        self.top -= 1
        return res

    def peek(self):
        return self.arr[self.top]
        
    def isEmpty(self):
        return self.top == -1

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
