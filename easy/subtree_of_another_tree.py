"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Time: O(N) -> Size of Big tree
Space: O(N) -> Size of Big tree
"""
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.is_same(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t);

    def is_same(self, s, t):
        if not s and not t:
            return True;
        if not s or not t:
            return False;
        return s.val == t.val and self.is_same(s.left, t.left) and self.is_same(s.right, t.right)
