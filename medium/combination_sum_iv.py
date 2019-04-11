"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Time: O(NlogN)
Space: O(N)
""" 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Similar to coin change
        """
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(1,target+1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[target]