def lnds(A):
	return lnds_(A, len(A)-2, 1, A[-1])

def lnds_(A, i, length, prev):
	if i < 0:
		return length
	curr = A[i]
	res1 = 0
	if curr <= prev:
		res1 = lnds_(A, i-1, length+1, curr)
	res2 = lnds_(A, i-1, length, prev)
	return max(res1, res2)

assert lnds([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]) == 4

def lndsDP(A):
	dp = [1 for i in xrange(len(A))]
	res = 0
	for i in xrange(1, len(A)):
		prev_len = 0
		for j in xrange(i):
			if A[j] <= A[i]:
				prev_len = max(dp[j], prev_len)
		dp[i] = prev_len + 1
		res = max(dp[i], res)
	return res

assert lndsDP([0, 8, 4, 12, 2, 10, 6, 14, 1, 9]) == 4
