def edit(s1, s2):
	return edit_(s1, s2, len(s1)-1, len(s2)-1, 0)

def edit_(s1, s2, p1, p2, d):
	if p1 < 0: return d + p2 + 1
	if p2 < 0: return d + p1 + 1
	if s1[p1] == s2[p2]:
		return edit_(s1, s2, p1-1, p2-1, d)
	insert = edit_(s1, s2, p1-1, p2, d+1)
	remove = edit_(s1, s2, p1, p2-1, d+1)
	replace = edit_(s1, s2, p1-1, p2-1, d+1)
	return min(insert, remove, replace)

def editDP(s1, s2):
	dp = [[0 for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
	for i in xrange(1, len(s1)+1):
		dp[i][0] = i
	for i in xrange(1, len(s2)+1):
		dp[0][i] = i
	for i in xrange(1, len(s1)+1):
		for j in xrange(1, len(s2)+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				insert = dp[i-1][j] + 1
				remove = dp[i][j-1] + 1
				replace = dp[i-1][j-1] + 1
				dp[i][j] = min(insert, remove, replace)
	return dp[-1][-1]

assert edit("geek", "gesek") == 1
assert edit("cat", "cut") == 1
assert edit("sunday", "saturday") == 3

assert editDP("geek", "gesek") == 1
assert editDP("cat", "cut") == 1
assert editDP("sunday", "saturday") == 3
