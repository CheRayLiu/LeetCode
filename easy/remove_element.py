class Solution:
    """
    O(N) time, O(1) space
    swap the not val elements to the front each time it occurs
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index +=1
        return index
