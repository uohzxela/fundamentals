RED = 0
WHITE = 1
BLUE = 2

def dutch_flag_partition(A, p):
	smaller = 0
	for i in xrange(len(A)):
		if A[i] < p:
			A[i], A[smaller] = A[smaller], A[i]
			smaller += 1

	larger = len(A) - 1
	for i in xrange(len(A)-1, -1, -1):
		if A[i] < p: break
		if A[i] > p:
			A[i], A[larger] = A[larger], A[i]
			larger -= 1

	return A

assert dutch_flag_partition([2,2,1,0,0,1,2,0], WHITE) == [0,0,0,1,1,2,2,2]
print dutch_flag_partition([2,2,0,0,1,1,2,0], RED)
print dutch_flag_partition([2,2,0,0,1,1,2,0], BLUE)