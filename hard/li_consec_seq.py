"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Time: O(N)
Space: O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for num in nums:
            if num - 1 not in nums:
                next =  num + 1
                while (next in nums):
                    next += 1
                best = max(best, next - num)
                
        return best
