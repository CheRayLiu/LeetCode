"""
Given an integer array nums, find the contiguous subarray within an array 
(containing at least one number) which has the largest product.
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max_prod = min_prod = nums[0]
        for num in nums[1:]:
            prev_max = max_prod
            max_prod = max(num, max_prod*num, min_prod*num)
            min_prod = min(num, prev_max*num, min_prod*num)
            res = max(res, max_prod)
        return res