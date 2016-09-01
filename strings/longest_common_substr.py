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
			# because of this line, we have to keep track of the maxLen
			# as it is not collected at the last element, e.g. dp[-1][-1]
			# compare this line with longest_common_subseq.py
			else: dp[i][j] = 0
	print maxLen
	return s1[longestEnd-maxLen:longestEnd]

def lcsR(s1, s2):
	return lcsR_(s1, s2, len(s1)-1, len(s2)-1, 0, 0)

def lcsR_(s1, s2, i, j, l, m):
	if i < 0 or j < 0: return m
	if s1[i] == s2[j]: return lcsR_(s1, s2, i-1, j-1, l+1, max(m, l+1))
	return max(lcsR_(s1, s2, i-1, j, 0, m), lcsR_(s1, s2, i, j-1, 0, m))

print lcs("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
print lcsR("OldSitez", "NewSiteSitez")
