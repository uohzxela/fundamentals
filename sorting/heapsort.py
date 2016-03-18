from priority_queue import PriorityQueue

def make_heap(A):
	pq = PriorityQueue()
	for i in xrange(len(A)):
		pq.insert(A[i])
	return pq

def heapsort(A):
	pq = make_heap(A)
	for i in xrange(len(A)):
		A[i] = pq.extract_min()

A = [23, 21, 5, 9, 10, 1, 8, 3, 0,-1, -10]
heapsort(A)
print A 
