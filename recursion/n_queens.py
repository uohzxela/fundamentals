def n_queens(n):
	A = []
	for i in xrange(n):
		A.append(i+1)
	permutate(A, 0)

def is_valid(A, k):
	for i in xrange(k):
		if k-i == abs(A[k]-A[i]):
			return False
	return True

def permutate(A, k):
	if k == len(A):
		print A
	for i in xrange(k, len(A)):
		A[i], A[k] = A[k], A[i]
		if is_valid(A, k):
			permutate(A, k+1)
		A[i], A[k] = A[k], A[i]

n_queens(4)