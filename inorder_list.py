from BST import BST

def inorder_list(root):
    if root == None:
        return []
        
    leftside = inorder_list(root.left)
    rightside = inorder_list(root.right)
    
    ans = [root.data]
    return leftside + ans + rightside
    
    
arr = [54,12,5,8,3,7,0,23]
tree = BST()
for i in arr:
    tree.insert(i)
    
# ~ tree.traverse()
# ~ print()

ans = inorder_list(tree.root)
for i in range(len(ans)-1):
    if ans[i] > ans[i+1]:
        print("False")
        break
    if i == len(ans)-2:
        print("True")
