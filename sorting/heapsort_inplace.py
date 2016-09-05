def heapsort(A):
	buildMaxHeap(A)
	n = len(A)-1
	for i in xrange(n, 0, -1):
		A[0], A[i] = A[i], A[0]
		# why i-1? because the elements at index i and beyond are already sorted.
		siftDown(A, 0, i-1)
	return A

def siftDown(A, i, n):
	left = i*2+1
	right = i*2+2
	largest = i
	if left <= n and A[left] > A[largest]: largest = left
	if right <= n and A[right] > A[largest]: largest = right
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		siftDown(A, largest, n)

# O(N)
def buildMaxHeap(A):
	n = len(A) - 1
	for i in xrange(n/2, -1, -1):
		siftDown(A, i, n)


assert heapsort([5,6,2,10,3,-1,11,1,0,7, 4]) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 10, 11]