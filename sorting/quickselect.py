def quickselect(A, k):
	return select(A, 0, len(A)-1, k)


def select(A, l, h, k):
	if l > h: return
	p = partition(A, l, h)
	if p == k: 
		return A[p]
	elif p < k: 
		return select(A, p+1, h, k)
	else:
		return select(A, l, p-1, k)


def partition(A, l, h):
	p = h
	firsthigh = l
	for i in xrange(l, h):
		if A[i] < A[p]:
			A[i], A[firsthigh] = A[firsthigh], A[i]
			firsthigh += 1
	A[p], A[firsthigh] = A[firsthigh], A[p]
	return firsthigh 


assert quickselect([7], 0) == 7
assert quickselect([7, 10, 4, 3, 20, 15], 2) == 7
assert quickselect([7, 10, 4, 3, 20, 15], 3) == 10
