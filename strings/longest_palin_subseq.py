class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in xrange(n):
            dp[i][i] = 1
        for sublen in xrange(1, n+1):
            for l in xrange(n-sublen):
                r = l + sublen
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l+1][r-1]
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return dp[0][-1]
        
    def helper(self, s, l, r):
        if l == r:
            return 1
        if l > r:
            return 0
        if s[l] == s[r]:
            return 2 + self.helper(s, l+1, r-1)
        else:
            return max(self.helper(s, l+1, r), self.helper(s, l, r-1))