def interleaving(s1, s2, s3):
	if len(s1) + len(s2) != len(s3):
		return False
	return interleaving_(s3, s1, s2, len(s1)-1, len(s2)-1)

def interleaving_(s, s1, s2, p1, p2):
	if p1 < 0:
		return s[:p2+1] == s2[:p2+1]
	if p2 < 0:
		return s[:p1+1] == s1[:p1+1]
	return ( (s[p1+p2+1] == s2[p2] and interleaving_(s, s1, s2, p1, p2-1)) or
			 (s[p1+p2+1] == s1[p1] and interleaving_(s, s1, s2, p1-1, p2)))


def interleavingDP(s1, s2, s):
	if len(s1) + len(s2) != len(s): return False
	dp = [[False for j in xrange(len(s2)+1)] for i in xrange(len(s1)+1)]
	dp[0][0] = True
	for i in xrange(1, len(s1)+1):
		if dp[i-1][0]:
			dp[i][0] = s[i-1] == s1[i-1]
		else:
			break
	for i in xrange(1, len(s2)+1):
		if dp[0][i-1]:
			dp[0][i] = s[i-1] == s2[i-1]
		else:
			break
	for i in xrange(1, len(s1)+1):
		for j in xrange(1, len(s2)+1):
			dp[i][j] = ((s[i+j-1] == s1[i-1] and dp[i-1][j]) 
						or (s[i+j-1] == s2[j-1] and dp[i][j-1]))
	return dp[-1][-1]

print interleaving("aabcc", "dbbca", "aadbbcbcac")
print interleaving("aabcc", "dbbca", "aadbbbaccc")

print interleavingDP("aabcc", "dbbca", "aadbbcbcac")
print interleavingDP("aabcc", "dbbca", "aadbbbaccc")

