# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = []
        
        q.append(root)
        q.append(root)
        
        while q:
            t1 = q.pop()
            t2 = q.pop()
            
            if t1 == None and t2 == None:
                continue
                
            if t1 == None or t2 == None:
                return False
            
            if t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
            
        return True