class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Brute force: Find all subarrays and compare with max water
        max_water = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                max_water = max(max_water, min(height[i],height[j])*(j-i))
        return max_water
        """
        
        """
        O(N)
        If left height smaller than right, move left inside, otherwise move right in
        """
        left, right, max_water = 0, len(height)-1, 0
        
        while left < right:
            max_water =  max(max_water, min(height[left],height[right])*(right-left))
            if height[right] > height[left]:
                left +=1
            else:
                right -=1
        return max_water