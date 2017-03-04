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

M0 = [[1,2],[3,4]]
M1 = [[1,2,3],[4,5,6],[7,8,9]]
M2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

assert rotate(M0) == [[3,1],[4,2]]
assert rotate(M1) == [[7,4,1],[8,5,2],[9,6,3]]
assert rotate(M2) == [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
