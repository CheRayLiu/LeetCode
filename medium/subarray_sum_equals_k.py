"""
Given an array of integers and an integer k, you need to 
find the total number of continuous subarrays whose sum equals to k.
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_dict = {0:1}
        pre_sum = res = 0
        
        for num in nums:
            pre_sum += num
            res += sum_dict.get(pre_sum-k, 0)
            sum_dict[pre_sum] = sum_dict.get(pre_sum, 0) + 1
        return res