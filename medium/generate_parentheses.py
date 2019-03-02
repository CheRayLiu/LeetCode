"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Time: ?
Space: O(N) 
"""
class Solution:
    def generateParenthesis(self, n):
        self.all_paren = []
        paren_str = ""
        self.backtrack_paren(n,n,paren_str)
        return self.all_paren
    def backtrack_paren(self,open,close,paren_str):
        if open == 0 and close == 0:
            self.all_paren.append(paren_str)
            return
        if open > 0:
            self.backtrack_paren(open-1,close,paren_str + "(")
        if close > open:
            self.backtrack_paren(open,close-1,paren_str + ")")