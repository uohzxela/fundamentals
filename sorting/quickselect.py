def quickselect(A, k):
	return select(A, 0, len(A)-1, k)

def select(A, l, h, k):
	# if l == h: 
	# 	return A[l]
	if l > h: return None
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

print quickselect([13, 2, 5], 2)