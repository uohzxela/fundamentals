import heapq
def merge(arrays):
	n, k = len(arrays[0]), len(arrays)
	h = []
	res = []
	for i in xrange(k):
		# (value, (i, j))
		heapq.heappush(h, (arrays[i][0], (i, 0)))
	print h
	while h and h[0][0] != float('inf'):
		v, (i,j) = heapq.heappop(h)
		res.append(v)
		if j+1 < n:
			heapq.heappush(h, (arrays[i][j+1], (i, j+1)))
		else:
			heapq.heappush(h, (float('inf'), (i, j+1)))
	return res

arrays = [[1,3,5,7], [2,4,6,8], [0,9,10,11]]

print merge(arrays)