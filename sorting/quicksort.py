def quicksort(A, l, h):
	if h > l:
		p = partition(A, l, h)
		quicksort(A, l, p-1)
		quicksort(A, p+1, h)

def partition(A, l, h):
	p = h #last element chosen as pivot
	firsthigh = l
	for i in range(l, h):
		if A[i] < A[p]:
			A[i], A[firsthigh] = A[firsthigh], A[i]
			firsthigh += 1
	A[p], A[firsthigh] = A[firsthigh], A[p]
	return firsthigh

A = [23, 21, 5, 9, 10, 4, 1, 1, 1, 1, 1, 1, 8, 3, 0,-1, -10]
quicksort(A, 0, len(A)-1)
print A

