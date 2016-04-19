def rabinKarp(t, s):
	if len(t) < len(s): return -1
	BASE = 10
	map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
	powerS = 1
	tHash = sHash = 0
	mod = 31

	for i in xrange(len(s)):
		powerS = 1 if i == 0 else powerS * BASE
		sHash = sHash * BASE + (map[s[i]])
		tHash = tHash * BASE + (map[t[i]])
	tHash %= mod
	sHash %= mod

	for i in xrange(len(s), len(t)):
		print 'tHash:', tHash
		print 'sHash:', sHash
		if tHash == sHash and t[i-len(s):i] == s:
			return i - len(s)
		# tHash = ((tHash - leftmost char) * BASE + new char) % mod
		tHash = ((tHash - (powerS * map[t[i-len(s)]])) * BASE + (map[t[i]])) % mod

	if tHash == sHash and t[len(t)-len(s):] == s:
		return len(t) - len(s)
	return -1


print rabinKarp("GACGCC", "CGC")
