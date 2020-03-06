# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    
    
    def isMirror(self, p: TreeNode, q: TreeNode):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False      
        if p.val != q.val:
            return False 
        
      #  if p.left != q.left or p.right != q.right:
       #     return False
    
        
        return self.isMirror(p.right,q.left) and self.isMirror(p.left, q.right)