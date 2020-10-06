# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))
        
        
        def check_balanced(root):
            if root is None:
                return BalancedStatusWithHeight(balanced=True, height=-1)
        
            leftResult = check_balanced(root.left)
            if not leftResult.balanced:
                return leftResult
            
            rightResult = check_balanced(root.right)
            if not rightResult.balanced:
                return rightResult
                
            is_balanced = abs(leftResult.height - rightResult.height) <= 1
            height = max(leftResult.height, rightResult.height) + 1
            return BalancedStatusWithHeight(is_balanced, height)
        
        return check_balanced(root).balanced