"""
Given a non-negative integer num represented as a string, remove k digits from the number 
so that the new number is the smallest possible.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) < k:
            return '0'
        stack = []
        
        for digit in num:
            while k > 0 and stack and int(stack[-1]) > int(digit):
                stack.pop()
                k-=1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        return ''.join(stack).lstrip('0') or "0"