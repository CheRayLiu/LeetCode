"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Time: O(N)
Space: O(N)
1. max counter
2. traversal through tree, compare depth with max when root is None
3. return max counter
"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.max = 0
        
        def traverse(root, depth):
            if not root:
                self.max = max(self.max, depth)
                return
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
        traverse(root, 0)
        
        return self.max
