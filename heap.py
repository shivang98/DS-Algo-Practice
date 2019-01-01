class Heap:
    HEAP_SIZE = 10
    
    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.current = -1
        
    def insert(self, data):
        if self.current >= Heap.HEAP_SIZE:
            print("Size full...")
            return
        else:
            self.current += 1
            self.heap[self.current] = data
            self.fixup(self.current)
             
    def fixup(self, index):
        parent = int((index-1)/2)
        while parent >= 0 and self.heap[index] > self.heap[parent]:
            temp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = temp
            index = parent
            parent = int((index-1)/2)
            
    def display(self):
        print(self.heap)
            
    def heapsort(self):
        for i in range(0,self.current+1):
            max_val = self.heap[0]
            print(max_val, end = " ")
            self.heap[0] = self.heap[self.current-i]
            self.heap[self.current-i] = max_val
            self.fixdown(0, self.current-1-i)
            
    def fixdown(self, index, upto):
        
        while index <= upto:
            
            leftchild = 2*index+1
            rightchild = 2*index+2
            
            if leftchild < upto:
                childToSwap = None
                
                if rightchild > upto:
                    childToSwap = leftchild
                else:
                    if self.heap[leftchild] > self.heap[rightchild]:
                        childToSwap = leftchild
                    else:
                        childToSwap = rightchild
                        
                if self.heap[childToSwap] > self.heap[index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                    
                index = childToSwap
            else:
                break
        

if __name__ == '__main__':
    hp = Heap()
    hp.insert(21)
    hp.insert(10)
    hp.insert(23)
    hp.insert(5)
    hp.insert(2)
    hp.insert(66)
    hp.display()
    hp.heapsort()
