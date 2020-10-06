# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
         return not root or self.checkSymmetry(root.left, root.right)
            
    def checkSymmetry(self, subTreeA, subTreeB):
        if not subTreeA and not subTreeB:
            return True
        elif subTreeA and subTreeB:
            return (subTreeA.val == subTreeB.val and self.checkSymmetry(subTreeA.left,subTreeB.right) and self.checkSymmetry(subTreeA.right, subTreeB.left))
        return False
    