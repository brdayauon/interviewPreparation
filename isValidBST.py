# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        inOrder = float('-inf')
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= inOrder:
                return False
            
            inOrder = root.val
            root = root.right
            
        return True