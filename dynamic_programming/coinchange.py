"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for i in xrange(amount+1)]
        dp[0] = 1
        for coin in coins:
        	"""
        	Note that the inner loop is not reversed (contrast this with knapsack.py)
        	This is because a coin can be used infinite number of times,
        	whereas for the knapsack solution, an item can only be used once.
        	So when we reverse the inner loop, we avoid using the item more than once.
        	Vice-versa, when we don't reverse the inner loop, we can reuse the current coin infinitely.
        	"""
            for i in xrange(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]