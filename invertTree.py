# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        leftTree = self.invertTree(root.left)
        rightTree = self.invertTree(root.right)
        
        root.left = rightTree
        root.right = leftTree
        
        return root