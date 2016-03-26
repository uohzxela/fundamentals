# references:
# http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/
# http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/Text/Matching-KMP1.html
# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
def kmp(p, s):
	m, n = len(p), len(s)
	print s
	print p
	if not m: return 0
	lps = [0]*(m) # longest proper suffix of prefix
	j = 0 # for pattern
	i = 0 # for string
	computeLPS(p, m, lps)
	while i < n:
		if p[j] == s[i]:
			i += 1
			j += 1
		if j == m:
			print "pattern index found at",
			return i-j
		elif i < n and p[j] != s[i]:
			if j != 0: j = lps[j-1]
			else: i += 1
	return -1


def computeLPS(p, m, lps):
	len = 0 # length of the previous longest prefix suffix
	lps[0] = 0
	i = 1
	while i < m:
		if p[i] == p[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			if len != 0:
				len = lps[-1]
			else:
				lps[i] = 0
				i += 1

print kmp("ABABCABAB", "ABABDABACDABABCABAB")