def wordBreak(s, words):
	return wordBreak_(s, 0, 0, set(words))

def wordBreak_(str, s, e, words):
	if e >= len(str):
		return s == e
	if str[s:e+1] in words:
		return wordBreak_(str, e+1, e+1, words) or wordBreak_(str, s, e+1, words)
	else:
		return wordBreak_(str, s, e+1, words)

def wordBreakDP(str, words):
	words = set(words)
	n = len(str)
	dp = [False for j in xrange(n+1)]
	dp[0] = True
	for i in xrange(1, n+1):
		if dp[i-1]:
			s = i
			for e in xrange(s, n+1):
				if str[s-1:e] in words:
					dp[e] = True
	return dp[-1]


print wordBreak('applepieapplea', ['apple', 'pie'])
print wordBreakDP('appleapplepie', ['appleapple', 'applepie', 'apple'])