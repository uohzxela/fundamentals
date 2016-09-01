def lcs(s1, s2):
	return lcs_(s1, s2, len(s1)-1, len(s2)-1)

def lcs_(s1, s2, p1, p2):
	if p1 < 0 or p2 < 0: return 0
	if s1[p1] == s2[p2]:
		return 1 + lcs_(s1, s2, p1-1, p2-1)
	else:
		return max(lcs_(s1,s2,p1,p2-1), lcs_(s1, s2, p1-1, p2))

# tail call optimization
def lcs_with_acc(s1, s2):
	return lcs_with_acc_(s1, s2, len(s1)-1, len(s2)-1, 0)

def lcs_with_acc_(s1, s2, p1, p2, acc):
	if p1 < 0 or p2 < 0:
		return acc
	if s1[p1] == s2[p2]:
		return lcs_with_acc_(s1, s2, p1-1, p2-1, acc+1)
	res1 = lcs_with_acc_(s1, s2, p1-1, p2, acc)
	res2 = lcs_with_acc_(s1, s2, p1, p2-1, acc)
	return max(res1, res2)

# res (max length of common subseq) is saved at the last element, e.g. dp[-1][-1]
def lcsDP(s1, s2):
	m, n = len(s1), len(s2)
	dp = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
	for i in xrange(1, m+1):
		for j in xrange(1, n+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				# because of this line, the res is collected at the last element, e.g. dp[-1][-1]
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])

	lcs = []
	p1, p2 = m, n
	while p1 > 0 and p2 > 0:
		if s1[p1-1] == s2[p2-1]:
			p1 -= 1
			p2 -= 1
			lcs.append(s1[p1])
		elif dp[p1-1][p2] > dp[p1][p2-1]:
			p1 -= 1
		else:
			p2 -= 1
	lcs.reverse()
	return dp[-1][-1], ''.join(lcs)

assert lcs('ABCDGH', 'AEDFHR') == 3
assert lcs_with_acc('ABCDGH', 'AEDFHR') == 3
assert lcsDP('ABCDGH', 'AEDFHR') == (3, 'ADH')
assert lcsDP('AGGTAB', 'GXTXAYB') == (4, 'GTAB')