def  lps(s):
    n = len(s)
    dp = [[0 for x in xrange(n)] for x in xrange(n)]
    for i in xrange(n):
        dp[i][i] = 1
    
    for sublen in xrange(2, n+1):
        for i in xrange((n-sublen) + 1):
            j = i + (sublen-1)
            if s[i] == s[j] and sublen == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][-1]

assert lps("BBABCBCAB") == 7