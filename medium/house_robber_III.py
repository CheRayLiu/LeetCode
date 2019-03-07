"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, 
called the "root." Besides the root, each house has one and only one parent house. After a tour, 
the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return max(self.traverse_house(root))
        
    def traverse_house(self, node):
        if not node:
            return (0,0)
        left,right = self.traverse_house(node.left), self.traverse_house(node.right)
        
        cur = left[1] + node.val + right[1]
        
        later =  max(left) + max(right)
        
        return (cur, later)