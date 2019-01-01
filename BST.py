class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BST:
    
    def __init__(self):
        self.root = None
        self._test = 10
        
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(self.root, data)
    
    def insert_node(self, node, data):
        if node.data > data:
            if node.left:
                self.insert_node(node.left, data)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(node.right, data)
            else:
                node.right = Node(data)
                
    def get_min(self):
        node = self.root
        minimum = node.data
        while node.left:
            node = node.left
            minimum = node.data
        return minimum
        
    def get_max(self):
        node = self.root
        maximum = node.data
        while node.right:
            node = node.right
            maximum = node.data
        return maximum
        
    def traverse(self):
        if self.root:
            self.inorder(self.root)
            
    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        print(node.data, end = " ")
        self.inorder(node.right)
        
    def delete(self, data):
        if self.root:
           self.root = self.delete_node(data, self.root)
        
    def delete_node(self, data, node):
        
        if not node:
            return None
            
        if data < node.data:
            node.left = self.delete_node(data, node.left)
        elif data > node.data:
            node.right = self.delete_node(data, node.right)
        else:
            if not node.left and not node.right:
                print("Deleting leaf node...")
                del node
                return None
            
            if not node.left:
                print("Replacing with right leaf...")
                temp = node.right
                del node
                return temp
            elif not node.right:
                print("Replacing with left leaf...")
                temp = node.left
                del node
                return temp
            
            print("Getting maximum from left-subtree...")
            pred = self.get_pred(node.left)
            node.data = pred.data
            node.left = self.delete_node(pred.data, node.left)
            
        return node
                
    def get_pred(self, node):
        if node.right:
            return self.get_pred(node.right)
        return node

if __name__ == '__main__':

    arr = [54,12,5,8,3,7,0,23]
    tree = BST()
    for i in arr:
        tree.insert(i)
        
    tree.traverse()
    print()
    print(tree.get_min())
    tree.delete(5)
    tree.traverse()
