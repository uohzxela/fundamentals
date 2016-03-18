# a = [10, 30, 5, 60]
a = [10, 20, 30, 40, 30]
# def m(a):
# 	cache = {}
# 	return mc(a, len(a)-2, a[-1], 0, cache)

# def mc(a, i, end, curr, cache):
# 	if i < 1: 
# 		cache[(i, end)] = curr
# 		return curr
# 	curr1 = a[i-1] * a[i] * end + curr
# 	res1 = mc(a, i-1, end, curr1, cache)
# 	curr2 = a[0] * a[i] * end + curr
# 	res2 = mc(a, i-1, a[i], curr2, cache)
# 	cache[(i, end)] = min(res1, res2)
# 	return min(res1, res2)

# print m(a)

def m(a):
	return mc(a, 1, len(a)-1)

def mc(a, i, j):
	if i == j: return 0
	min = float('inf')
	curr = 0
	for k in xrange(i, j):
		curr = mc(a, i, k) + mc(a, k+1, j) + (a[i-1] * a[k] * a[j])
		if curr < min:
			min = curr
	return min 

def mc_dp(a):
	n = len(a)
	m = [[0 for x in range(n)] for x in range(n)]
	# L is chain length.
	for L in range(2, n):
		for i in range(1, n-L+1):
			j = i+L-1
			m[i][j] = float('inf')
			for k in range(i, j):
				q = m[i][k] + m[k+1][j] + a[i-1]*a[k]*a[j]
				if q < m[i][j]:
					m[i][j] = q
	return m[1][n-1]

print m(a)
print mc_dp(a)