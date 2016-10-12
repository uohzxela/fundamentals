def count_ways_to_top(n, step_size):
	if n < 0: return 0
	if n == 0: return 1
	res = 0
	for i in xrange(1, step_size+1):
		res += count_ways_to_top(n-i, step_size)
	return res

def count_ways_to_topDP(n, step_size):
	dp = [0 for i in xrange(n+1)]
	dp[0] = 1
	for i in xrange(1, n+1):
		for j in xrange(1, step_size+1):
			if i-j >= 0:
				dp[i] += dp[i-j]
	return dp[-1]

assert count_ways_to_top(5, 2) == 8
assert count_ways_to_top(4, 2) == 5
assert count_ways_to_topDP(5, 2) == 8
assert count_ways_to_topDP(4, 2) == 5