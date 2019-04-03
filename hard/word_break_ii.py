"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences.
Time: ??
Space: O(N)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        solution = {}
        solution[n] = [""]
        wordDict = set(wordDict)
        
        def solve(i):
            if i not in solution:
                solution[i] = [ s[i:j] + (tail and (" " + tail))
                                for j in range(i, n+1)
                                if s[i:j] in wordDict
                                for tail in solve(j)]
            return solution[i]
        solve(0)
        print(solution)
        return solution[0]