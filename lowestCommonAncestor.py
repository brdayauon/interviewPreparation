# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        status = collections.namedtuple('status', ('num_target_nodes', 'ancestor'))
        
        def lca_helper(root, nodeA, nodeB):
            if root is None:
                return status(num_target_nodes = 0, ancestor = None)
            
            leftResult = lca_helper(root.left, nodeA, nodeB)
            if leftResult.num_target_nodes == 2:
                return leftResult
            
            rightResult = lca_helper(root.right, nodeA, nodeB)
            if rightResult.num_target_nodes == 2:
                return rightResult
            
            num_target_nodes = (leftResult.num_target_nodes + rightResult.num_target_nodes + (nodeA,nodeB).count(root))
            
            return status(num_target_nodes, root if num_target_nodes == 2 else None)
        
        return lca_helper(root, p,q).ancestor