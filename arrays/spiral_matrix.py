m1 = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8],
 [ 9, 10, 11, 12 ],
 [13, 14, 15, 16]
]

m2 = [
 [ 1, 2, 3],
 [ 4, 5, 6],
 [ 7, 8, 9]
]

m3 = [
 [ 1, 2],
 [ 3, 4]
]

def spiral(m):
	n = len(m)-1
	res = []
	i = 0
	while n > 0:
		for j in xrange(n):
			res.append(m[i][i+j])
		for j in xrange(n):
			res.append(m[i+j][i+n])
		for j in xrange(n):
			res.append(m[i+n][i+n-j])
		for j in xrange(n):
			res.append(m[i+n-j][i])
		i += 1
		n -= 2
	if n == 0:
		res.append(m[i][i])
	return res

assert spiral(m1) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
assert spiral(m2) == [1,2,3,6,9,8,7,4,5]
assert spiral(m3) == [1,2,4,3]
