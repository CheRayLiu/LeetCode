"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        left = 0
        right = 0
        min_left = 0
        char_dict = {}
        min_len = len(s)
        count = 0
        min_str = ""
        for char in t:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        for right in range(len(s)):
            if s[right] in char_dict:
                char_dict[s[right]] -= 1
                if char_dict[s[right]] >= 0:
                    count += 1
                while (count == len(t)):
                    if (right-left+1 <= min_len):
                        min_left = left
                        min_len = right-left+1
                        min_str = s[min_left:min_left+min_len]
                    if s[left] in char_dict:
                        char_dict[s[left]] += 1
                        if char_dict[s[left]] > 0:
                            count -= 1
                    left += 1
        if min_len > len(s):
            return ""
        return min_str