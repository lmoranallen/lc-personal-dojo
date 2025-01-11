class TreeNode:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
    

def kthSmallest(self, root: list[TreeNode], k: int) -> int:
    
    curr = root
    n = 0
    stack = []

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        elem = stack.pop()
        

        if elem is not None:
            n += 1
            if n == k:
                return elem.val
            
            curr = elem.right
