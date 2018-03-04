import numpy as np

def rotate(M):
	n = len(M)
	print 'before:'
	print np.array(M)
	for i in xrange(n/2):
		for j in xrange(i, n-i-1):
			tmp1 = M[i][j]
			tmp2 = M[j][n-1-i]
			tmp3 = M[n-1-i][n-1-j]
			tmp4 = M[n-1-j][i]

			M[i][j] = tmp4
			M[j][n-1-i] = tmp1
			M[n-1-i][n-1-j] = tmp2
			M[n-1-j][i] = tmp3
	print 'after:'
	print np.array(M)
	print
	return M

def rotate2(A):
	n = len(A)
	# swap A[i][j] and A[j][i]
	for i in xrange(n):
		for j in xrange(i, n):
			A[i][j], A[j][i] = A[j][i], A[i][j]
	# reverse each row
	for i in xrange(n):
		s, e = 0, n - 1
		while s < e:
			A[i][s], A[i][e] = A[i][e], A[i][s]
			s, e = s + 1, e - 1
	return A

M0 = [[1,2],[3,4]]
M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# executing these will mutate the matrices so they are commented out

# assert rotate(M0) == [[3,1],[4,2]]
# assert rotate(M1) == [[7,4,1],[8,5,2],[9,6,3]]
# assert rotate(M2) == [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

assert rotate2(M0) == [[3,1],[4,2]]
assert rotate2(M1) == [[7,4,1],[8,5,2],[9,6,3]]
assert rotate2(M2) == [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
