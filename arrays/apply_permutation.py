def apply_permutation(A, P):
	for i in xrange(len(A)):
		while P[i] != i:
			j = P[i]
			A[i], A[j] = A[j], A[i]
			P[i], P[j] = P[j], P[i]
	return A

def apply_permutation2(A, P):
	for i in xrange(len(A)):
		next = i
		while P[next] >= 0:
			A[i], A[P[next]] = A[P[next]], A[i]
			temp = P[next]
			P[next] = P[next] - len(P)
			next = temp
	# P is restored
	for i in xrange(len(P)):
		P[i] += len(P)

	return A 

assert apply_permutation(['a','b','c','d'], [2,0,1,3]) == ['b','c','a','d']
assert apply_permutation2(['a','b','c','d'], [2,0,1,3]) == ['b','c','a','d']
assert apply_permutation(['a','b','c','d'], [3,2,1,0]) == ['d','c','b','a']
assert apply_permutation2(['a','b','c','d'], [3,2,1,0]) == ['d','c','b','a']