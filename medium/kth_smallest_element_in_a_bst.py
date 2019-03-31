"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.kth = 0
        def search_k(root, k):
            if not root:
                return
            search_k(root.left, k)
            self.count += 1
            if self.count == k:
                self.kth = root.val
            search_k(root.right, k)
        search_k(root,k)
        return self.kth
