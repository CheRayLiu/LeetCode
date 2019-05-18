class Solution:
    """
    O(N) time, O(1) space
    swap the not val elements to the front each time it occurs
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        val_start = -1
        val_len = 0
        val_count = 0
        """
        [3,2,2,3], 3
        """
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index +=1
        return index
