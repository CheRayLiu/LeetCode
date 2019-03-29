"""
Given a string, find the length of the longest substring without repeating characters.
Time: O(N)
Space: O(N)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            max_len = max(max_len, i-start+1)
            used[s[i]] = i
        return max_len