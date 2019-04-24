"""
Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, 
implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. 
Note that an unlimited amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1.
"""
def minNumberOfCoinsForChange(n, denoms):
		memo = [float('inf')] * (n+1)
		memo[0] = 0

		for coin in denoms:
			for amount in range(1,n+1):
				if amount >= coin:
					memo[amount] = min(memo[amount-coin] + 1,memo[amount])
		return memo[-1] if memo[-1] != float('inf') else -1
