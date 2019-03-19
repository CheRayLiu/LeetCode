"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        write_index = 1
        
        for i in range(1,len(nums)):
            if nums[write_index-1] != nums[i]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index