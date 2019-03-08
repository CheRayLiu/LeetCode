"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Eg.
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Time: O(N^2)
Complexity: O(N)
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = ""
        for index in range(len(s)):
            cur_string = self.middle_out(s,index,index)
            if len(cur_string) > len(max_str):
                max_str = cur_string
            cur_string = self.middle_out(s,index,index+1)
            if len(cur_string) > len(max_str):
                max_str = cur_string
        return max_str     
    def middle_out(self,s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right] #Important