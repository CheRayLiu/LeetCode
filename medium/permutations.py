"""
Given a collection of distinct integers, return all possible permutations.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def possible(i):
            if i == len(nums) - 1:
                res.append(nums[:])
            else:
                for j in range(i,len(nums)):
                    nums[i], nums[j] = nums[j], nums[i]
                    possible(i+1)
                    nums[i], nums[j] = nums[j], nums[i]
        possible(0)
        return res