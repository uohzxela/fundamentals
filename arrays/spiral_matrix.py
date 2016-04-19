m = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8],
 [ 9, 10, 11, 12 ],
 [13, 14, 15, 16]
]
# not finished yet
def spiral(m):
	n = len(m)
	i = n-1
	res = []
	while i >= 0:
		if i == n - i - 1:
			res.append(m[i][i])
			break
		for j in xrange(i):
			res.append(m[n-i-1][j])
		for j in xrange(i):
			res.append(m[j][i])
		for j in xrange(i):
			res.append(m[i][i-j])
		for j in xrange(i):
			res.append(m[i-j][n-i-1])
		i -= 1
	print res

spiral(m)

