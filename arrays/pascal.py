def pascal(n):
	arr = []
	for line in xrange(1,n+1):
		c = 1
		for i in xrange(1, line+1):
			print c,
			c = c * (line - i)/i
		print 
		
def pascal2(n):
	if n == 0: return []
	res = [[1]]
	for i in xrange(1, n):
		res.append([1])
		for j in xrange(1, i):
			res[i].append(res[i-1][j] + res[i-1][j-1])
		res[i].append(1)
	for r in res:
		print r

pascal(6)
pascal(6)
