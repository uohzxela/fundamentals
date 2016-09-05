# O(n!)
def permutations(A):
	print_permutations(A, 0)

def print_permutations(A, p):
	if p == len(A):
		print_permutation(A)
		return
	for i in xrange(p, len(A)):
		A[i], A[p] = A[p], A[i]
		print_permutations(A, p+1)
		A[i], A[p] = A[p], A[i]

def print_permutation(A):
	print A

permutations([1,2,3])