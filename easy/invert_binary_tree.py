"""
Invert a binary tree.
Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def invert(root):
            if not root:
                return
            root.left, root.right =  root.right, root.left
            invert(root.left)
            invert(root.right)
        invert(root)
        return root
