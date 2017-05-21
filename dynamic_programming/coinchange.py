"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [sys.maxint for j in xrange(amount+1)]
        dp[0] = 0

        for coin in coins:
        	"""
        	Note that the inner loop is not reversed (contrast this with knapsack.py)
        	This is because a coin can be used infinite number of times,
        	whereas for the knapsack solution, an item can only be used once.
        	So when we reverse the inner loop, we avoid using the item more than once.
        	Vice-versa, when we don't reverse the inner loop, we can reuse the current coin infinitely.
        	"""
            for i in xrange(coin, amount+1):
                dp[i] = min(dp[i-coin]+1, dp[i])
        return -1 if dp[-1] == sys.maxint else dp[-1]
    
    def coinChange2D(self, coins, amount):
        dp = [[sys.maxint for j in xrange(amount+1)] for i in xrange(len(coins)+1)]
        for i in xrange(len(coins)+1):
            dp[i][0] = 0
        
        for i in xrange(1, len(coins)+1):
            for j in xrange(1, amount+1):
                dp[i][j] = dp[i-1][j]
                if j-coins[i-1] >= 0:
                    dp[i][j] = min(dp[i][j-coins[i-1]] + 1, dp[i-1][j])
        return -1 if dp[-1][-1] == sys.maxint else dp[-1][-1]
    
    def coinChangeRecursive(self, coins, amount, count, i):
        if amount < 0:
            return sys.maxint
        if i == len(coins):
            if amount == 0:
                return count
            return sys.maxint
        res1 = self.coinChangeRecursive(coins, amount, count, i+1)
        res2 = self.coinChangeRecursive(coins, amount-coins[i], count+1, i)
        return min(res1, res2)
