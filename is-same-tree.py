
class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

def isSameTree(p, q):
    
    if p is False and q is False:
        return True

    if p is False and q is True or p is True and q is False:
        return False
    
    if p.left is False and q.left is True or p.right is False and q.right is True:
        return False
    
    if p.left is True and q.left is False or p.right is True and q.right is False:
        return False
    
    else:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    

