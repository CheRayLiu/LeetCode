"""
Given a binary tree, 
find the lowest common ancestor (LCA) of two given nodes in the tree.

Time: O(N)
Space: O(N)
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
            if not root:
                return
            if root.val in (p.val, q.val):
                return root
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)
            
            return root if left and right else left or right
