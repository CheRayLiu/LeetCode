class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None]*len(nums)
        dp[0] = nums[0]
        max_num = dp[0]
        for i in range(1,len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            max_num = max(dp[i],max_num)
        return max_num
    