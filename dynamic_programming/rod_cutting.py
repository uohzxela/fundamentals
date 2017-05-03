def rod_cutting(n, prices):
	if n <= 0:
		return 0
	res = 0
	for i in xrange(n):
		res = max(prices[n-i] + rod_cutting(i, prices), res)
	return res

assert rod_cutting(8, [0, 1, 5, 8, 9, 10, 17, 17, 20]) == 22
assert rod_cutting(8, [0, 3, 5, 8, 9, 10, 17, 17, 20]) == 24
assert rod_cutting(4, [0, 1, 5, 8, 9]) == 10

def rod_cutting_dp(n, prices):
	if n <= 0:
		return 0
	dp = [0]*(len(prices))
	for i in xrange(1, len(prices)):
		for j in xrange(i):
			dp[i] = max(prices[i-j] + dp[j], dp[i])
	return dp[-1]

assert rod_cutting_dp(8, [0, 1, 5, 8, 9, 10, 17, 17, 20]) == 22
assert rod_cutting_dp(8, [0, 3, 5, 8, 9, 10, 17, 17, 20]) == 24
assert rod_cutting_dp(4, [0, 1, 5, 8, 9]) == 10
