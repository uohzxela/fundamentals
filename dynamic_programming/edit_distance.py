class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for j in xrange(len(word2) + 1)] for i in xrange(len(word1) + 1)]
        for i in xrange(len(word1) + 1):
            dp[i][0] = i
        for j in xrange(len(word2) + 1):
            dp[0][j] = j

        for i in xrange(1, len(word1) + 1):
            for j in xrange(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert, remove, replace = dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]
                    dp[i][j] = min(insert, remove, replace) + 1

        return dp[-1][-1]
    
    def helper(self, word1, word2, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if word1[i] == word2[j]:
            return self.helper(word1, word2, i - 1, j - 1)

        insert = self.helper(word1, word2, i - 1, j)
        remove = self.helper(word1, word2, i, j - 1)
        replace = self.helper(word1, word2, i - 1, j - 1)
        return min(insert, remove, replace) + 1
