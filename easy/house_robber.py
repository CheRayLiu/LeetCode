"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Time: O(N)
Space: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. Rob cur and previous_2
        2. Rob previous
        """
        if not nums:
            return 0
        memo = [-1]*(len(nums)+1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1,len(nums)):
            memo[i+1] =  max(nums[i]+memo[i-1], memo[i])
        return memo[-1]