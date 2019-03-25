"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profit = float('inf'), 0
        
        for price in prices:
            min_price = min(price,min_price)
            profit = price - min_price
            max_profit = max(profit,max_profit)
            
        return max_profit