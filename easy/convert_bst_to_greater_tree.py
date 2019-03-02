"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key 
plus sum of all keys greater than the original key in BST.
Time: O(N)
Space: O(N)
"""
class Solution:
    def convertBST(self, root):
        self.sum = 0
        self.transform_bst(root)
        return root
    def transform_bst(self,node):
        if not node:
            return node
        self.transform_bst(node.right)
        node.val += self.sum
        self.sum = node.val
        self.transform_bst(node.left)