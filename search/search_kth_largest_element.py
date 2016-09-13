def find_kth_largest(A, k):
	return quickselect(A, 0, len(A)-1, len(A)-k)

def quickselect(A, s, e, k):
	if s > e: return
	p = partition(A, s, e)
	if p == k:
		return A[k]
	elif p < k:
		return quickselect(A, p+1, e, k)
	else:
		return quickselect(A, s, p-1, k)

def partition(A, s, e):
	p = e
	firsthigh = s
	for i in xrange(s, e):
		if A[i] < A[p]:
			A[i], A[firsthigh] = A[firsthigh], A[i]
			firsthigh += 1
	A[firsthigh], A[p] = A[p], A[firsthigh]
	return firsthigh

A = [3,1,-1,2]
assert find_kth_largest(A, 1) == 3
assert find_kth_largest(A, 2) == 2
assert find_kth_largest(A, 3) == 1
assert find_kth_largest(A, 4) == -1