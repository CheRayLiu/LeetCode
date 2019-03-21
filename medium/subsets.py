"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtrack(0, sorted(nums), [])
        return self.res
        
    def backtrack(self, index, nums, path):
        self.res.append(path)
        for i in range(index,len(nums)):
            self.backtrack(i+1, nums, path+[nums[i]])
