from BST import BST

def is_bst(node, ul = None, ll = None):
    
    if ul and node.data > ul: return False
    
    if ll and node.data < ll: return False
    
    is_left = True
    is_right = True
    
    if node.left:
        is_left = is_bst(node.left, node.data, ll)
    
    if node.right:
        is_right = is_bst(node.right, ul, node.data)
        
    return is_left and is_right
