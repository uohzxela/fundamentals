def heapsort(A):
	"""
	Time complexity: O(nlog n)
	"""
	A = heapify(A)
	for i in xrange(len(A)-1, 0, -1):
		A[0], A[i] = A[i], A[0]
		# why i-1? because the elements at index i and beyond are already sorted.
		A = bubble_down(A, 0, i-1)
	return A

def heapify(A):
	"""
	Time complexity: O(n)
	Turn an array into a max-heap.
	"""
	n = len(A)
	for i in xrange((n/2)-1, -1, -1):
		A = bubble_down(A, i, n-1)
	return A

def bubble_down(A, i, e):
	"""
	Time complexity: O(log n)
	"""
	left = i*2+1
	right = i*2+2

	max_idx = i
	if left <= e and A[left] > A[max_idx]:
		max_idx = left
	if right <= e and A[right] > A[max_idx]:
		max_idx = right
	if max_idx != i:
		A[max_idx], A[i] = A[i], A[max_idx]
		return bubble_down(A, max_idx, e)
	return A

assert heapsort([5, 6, 2, 10, 3, -1, 11, 1, 0, 7, 4]) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 10, 11]
assert heapsort([1, 3, 4]) == [1, 3, 4]
