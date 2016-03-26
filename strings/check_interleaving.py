def checkInterleaving_(s, s1, s2, i, j):
	if i < 0: return s[:j+1] == s2[:j+1]
	if j < 0: return s[:i+1] == s1[:i+1]
	res1 = s[i+j+1] == s1[i] and checkInterleaving_(s, s1, s2, i-1, j)
	res2 = s[i+j+1] == s2[j] and checkInterleaving_(s, s1, s2, i, j-1)
	return res1 or res2


def checkInterleaving(s, s1, s2):
	if len(s1) + len(s2) != len(s):
		print False
	else:
		print checkInterleaving_(s, s1, s2, len(s1)-1, len(s2)-1)

def checkInterleavingDp(s, s1, s2):
	if len(s1) + len(s2) != len(s):
		print False
		return
	n, m = len(s1), len(s2)
	dp = [[False for j in xrange(m+1)] for i in xrange(n+1)]
	dp[0][0] = True
	
	for i in xrange(1,n+1): 
		if s[i-1] == s1[i-1]: dp[i][0] = True
		else: break
	for j in xrange(1,m+1): 
		if s[j-1] == s2[j-1]: dp[0][j] = True
		else: break
	for i in xrange(1, n+1):
		for j in xrange(1, m+1):
			dp[i][j] = (s[i+j-1] == s1[i-1] and dp[i-1][j] or
						s[i+j-1] == s2[j-1] and dp[i][j-1])
	print dp[-1][-1]




checkInterleaving("1234", "123", "123")
checkInterleaving("112233", "123", "123")
checkInterleaving("123456", "123456", "")
checkInterleaving("123456", "", "123456")
checkInterleaving("12345678", "1234", "5678")
checkInterleaving("12345678", "1233", "5678")
checkInterleaving("112223", "122", "123")

print 'dp'

checkInterleavingDp("1234", "123", "123")
checkInterleavingDp("112233", "123", "123")
checkInterleavingDp("123456", "123456", "")
checkInterleavingDp("123456", "", "123456")
checkInterleavingDp("12345678", "1234", "5678")
checkInterleavingDp("12345678", "1233", "5678")
checkInterleavingDp("112223", "122", "123")
checkInterleavingDp("cbb", "db", "b")