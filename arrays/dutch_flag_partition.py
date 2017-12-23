def dutch_flag_partition(A, pivot_index):
	pivot = A[pivot_index]

	smaller = 0
	for i in xrange(len(A)):
		if A[i] < pivot:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1

	larger = len(A) - 1
	for i in xrange(len(A)-1, -1, -1):
		if A[i] < pivot:
			break
		if A[i] > pivot:
			A[i], A[larger] = A[larger], A[i]
			larger -= 1

	return A

assert dutch_flag_partition([2,2,1,0,0,1,2,0], 2) == [0,0,0,1,1,2,2,2]
assert dutch_flag_partition([2,2,1,2,0,1,0,0], 2) == [0,0,0,1,1,2,2,2]
assert dutch_flag_partition([2,2,0,0,1,1,2,0], 0) == [0, 0, 1, 1, 0, 2, 2, 2]
assert dutch_flag_partition([2,2,0,0,1,1,2,0], 2) == [0, 0, 0, 2, 2, 1, 1, 2]
