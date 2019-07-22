# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """
       Height of node is leave to root, bottom up approach
        
        keep track of level with cur_level
        
        Base case:
        When root is null, return -1
        
        leaf_by_level = max(left, right) + 1
        if len(res) <= leaf_by_level:
            res.append([root.val])
        else:
            res[leaf_by_level].append(root.val)
        """
        
        res = []
        
        self.leaf_by_level(root, res)
        
        return res
        
    def leaf_by_level(self, root, res):
        
        if not root:
            return -1
        
        left_lvl = self.leaf_by_level(root.left, res)
        right_lvl = self.leaf_by_level(root.right, res)
        root.left = None 
        root.right = None
        level = max(left_lvl, right_lvl) + 1
        
        if len(res) <= level:
            res.append([root.val])
        else:
            res[level].append(root.val)
        return level
        
        
        
        