
import collections


class TreeNode():
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None

def bfs(root: list[TreeNode]) -> list[list[int]]:
    # curr = root
    res = []

    q = collections.deque()
    q.append(root)

    while q:
        _N = len(q)
        level = []
        for i in range(_N):
            node = q.popleft()
            if node is not None:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res


# print(bfs([1,2,3,4,5,6,7]))
