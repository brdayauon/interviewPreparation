# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        q = deque() 
        depth = 0
        q.append(root)
        
        while True:
            nodect = len(q)
            if not nodect:
                return depth
            depth += 1
            
            while nodect:
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                nodect -= 1        
        
    
        
    #Recursive    ###if root == None:
    #        return 0
        
    #    leftTree = self.maxDepth(root.left)
    #    rightTree = self.maxDepth(root.right)
        
    #    return max(leftTree,rightTree) + 1
    ###