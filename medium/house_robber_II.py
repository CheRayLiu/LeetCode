"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Time: O(N)
Space: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. Rob first, leave last
        2. Rob last, leave first
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def rob_house(house):
            memo = [-1]*(len(house)+1)
            memo[0] = 0
            memo[1] = house[0]
            
            for i in range(1,len(house)):
                memo[i+1] = max(house[i]+memo[i-1], memo[i])
            return memo[-1]
        return max(rob_house(nums[1:]), rob_house(nums[:-1]))
