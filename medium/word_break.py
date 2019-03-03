"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Time: O(N*M) N= len(s), M=len(dict)
Space: O(N) N= len(s)
"""
class Solution:
    def wordBreak(self, s, wordDict):
        check_word = [False]*len(s)
        
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (check_word[i-len(w)] or i-len(w) == -1):
                    check_word[i] = True
        return check_word[-1]