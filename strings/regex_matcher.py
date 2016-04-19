class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False for j in xrange(n+1)] for i in xrange(m+1)]
        dp[0][0] = True

        for i in xrange(0, m+1):
            for j in xrange(1, n+1):
                if p[j-1] != '.' and p[j-1] != '*':
                    if i>0 and s[i-1] == p[j-1] and dp[i-1][j-1]:
                        dp[i][j] = True
                elif p[j-1] == '.':
                    if i>0 and dp[i-1][j-1]:
                        dp[i][j] = True
                elif j > 1:
                    if dp[i][j-1] or dp[i][j-2]:
                        dp[i][j] = True
                    elif i>0 and (p[j-2] == s[i-1] or p[j-2] == '.') and dp[i-1][j]:
                        dp[i][j] = True
        return dp[-1][-1]   


print Solution().isMatch("ab", ".*c")
print Solution().isMatch('aa', 'a*')
print Solution().isMatch("aab", "c*a*b")
print Solution().isMatch("aaa", "a*a")
print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")