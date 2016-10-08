def count_num_paths_to_xy(n, m):
	dp = [[0 for j in xrange(m)] for i in xrange(n)]
	for i in xrange(n):
		dp[i][0] = 1
	for i in xrange(m):
		dp[0][i] = 1
	for i in xrange(1, n):
		for j in xrange(1, m):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[-1][-1]

assert count_num_paths_to_xy(5, 5) == 70