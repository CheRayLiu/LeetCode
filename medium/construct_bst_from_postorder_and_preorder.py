"""
Given inorder and postorder traversal of a tree, construct the binary tree.
Time: O(N^2)
Space: O(log(N))
"""
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_index = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_index])
            root.right = self.buildTree(inorder[root_index+1:],postorder)
            root.left = self.buildTree(inorder[:root_index],postorder)
            return root