"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.
Time: O(nlogn + n*m)
Space: O(n)
"""
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x),x))
        max_word = ""
        for word in d:
            str_pt = 0
            word_pt = 0
            while (str_pt != len(s) and word_pt != len(word)):
                if s[str_pt] == word[word_pt]:
                    word_pt +=1
                str_pt += 1
            if word_pt == len(word):
                return word
        return max_word