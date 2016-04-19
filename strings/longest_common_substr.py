# dp[i][j] = 1 + dp[i-1][j-1] if s1[i-1] == s2[j-1]
# dp[i][j] = 0 if s1[i-1] != s2[j-1]
# base case: dp[0][0] = 0
def lcs(s1, s2):
	dp = [[0 for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
	maxLen = longestEnd = 0
	for i in xrange(1, len(s1)+1):
		for j in xrange(1, len(s2)+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
				if maxLen < dp[i][j]:
					maxLen = dp[i][j]
					longestEnd = i
			else: dp[i][j] = 0
	return s1[longestEnd-maxLen:longestEnd]


print lcs("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
