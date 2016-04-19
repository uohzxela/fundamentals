'''
longest common substring
insights: 
	the max length is not found at the bottom right cell.
	need to use a variable to store the max length when performing DP, and return it as the answer

'''
def lcs(a, b):
	return lcs_(a, b, len(a)-1, len(b)-1, 0, 0)

def lcs_(a, b, p1, p2, l, maxl):
	if p1 < 0 or p2 < 0: return maxl

	if a[p1] == b[p2]:
		return lcs_(a, b, p1-1, p2-1, l+1, max(maxl, l+1))
	else:
		res1 = lcs_(a, b, p1-1, p2, 0, maxl)
		res2 = lcs_(a, b, p1, p2-1, 0, maxl)
		return max(res1, res2)

#print lcs(a,b)

def lcs_dp(a, b):
	len_a, len_b = len(a)+1, len(b)+1
	m = [[0 for j in xrange(len_b)] for i in xrange(len_a)]
	count, final_a_pos = -1, None

	for i in xrange(1, len_a):
		for j in xrange(1, len_b):
			if a[i-1] == b[j-1]:
				m[i][j] = 1 + m[i-1][j-1]
				if count < m[i][j]:
					count = m[i][j]
					final_a_pos = i-1
			else: m[i][j] = 0

	LCS = []
	for i in xrange(count):
		LCS.insert(0, a[final_a_pos - i])

	print "LCS is", "\"" + ''.join(LCS) + "\"", "with a length of", count

a = "OldSite:GeeksforGeeks.org"
b = "NewSite:GeeksQuiz.com"
lcs_dp(a,b)