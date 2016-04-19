def lps1(s):
	n = len(s)
	dp = [[False for j in xrange(n)] for i in xrange(n)]
	for i in xrange(n):
		dp[i][i] = True

	for i in xrange(n-1):
		if s[i] == s[i+1]:
			dp[i][i+1] = True
	maxLen = 1
	longestBegin = 0
	for sLen in xrange(3, n+1):
		end = n - sLen + 1
		for i in xrange(end):
			j = i+sLen-1
			if s[i] == s[j] and dp[i+1][j-1]:
				maxLen = sLen
				longestBegin = i
				dp[i][j] = True
	return s[longestBegin: longestBegin + maxLen]

# print lps1("forgeeksskeegfor")
# print lps1("a")


def expand(s, l, r):
	n = len(s)
	while l >= 0 and r < n and s[l] == s[r]:
		l -= 1
		r += 1
	return l+1, r-1 

def lps2(s):
	maxLen = 1
	res_l, res_r = 0, 1
	for i in xrange(len(s)-1):
		l, r = expand(s, i, i)
		if r-l+1 > maxLen:
			maxLen = r-l+1
			res_l, res_r = l, r
		l, r = expand(s, i, i+1)
		if r-l+1 > maxLen:
			maxLen = r-l+1
			res_l, res_r = l, r
	return s[res_l: res_r+1]

print lps2("forgeeksskeegfor")