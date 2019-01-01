from BST import BST

def path(root, data):
    
    if root is None:
        return None
        
    if root.data == data:
        return [data]
        
    l1 = path(root.left, data)
    l2 = path(root.right, data)
    
    res = None
    if l1 is not None:
        res = [root.data] + l1
    
    if l2 is not None:
        res = [root.data] + l2
        
    return res

arr = [54,12,5,8,3,7,0,23]
tree = BST()
for i in arr:
    tree.insert(i)
    
tree.traverse()
print()

print(tree._test)
# ~ print(path(tree.root, 0))
