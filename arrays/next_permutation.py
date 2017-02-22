# 1. from right to left, find the first digit which violates the increasing property (partitionDigit)
# 2. from right to left, find the first digit > than partitionDigit (changeDigit)
# 3. swap changeDigit and partitionDigit
# 4. reverse all digits to the right of partitionIndex

def next_perm(A):
	p = -1
	# step 1
	for i in xrange(len(A)-2, -1, -1):
		if A[i] < A[i+1]:
			p = i
			break
	if p == -1: 
		return []
	# step 2
	for i in xrange(len(A)-1, -1, -1):
		if A[i] > A[p]: 
			A[i], A[p] = A[p], A[i]
			break
	# step 3
	reverse(A, p+1, len(A)-1)
	return A

def reverse(A, s, e):
	num_to_reverse = e - s + 1
	for i in xrange(num_to_reverse/2):
		A[s+i], A[e-i] = A[e-i], A[s+i]

assert next_perm([1,0,3,2]) == [1,2,0,3]
assert next_perm([0,1,2]) == [0,2,1]
assert next_perm([0,2,1]) == [1,0,2]
assert next_perm([1,0,2]) == [1,2,0]
assert next_perm([1,2,0]) == [2,0,1]
assert next_perm([2,0,1]) == [2,1,0]
assert next_perm([2,1,0]) == []
assert next_perm([6,2,1,5,4,3,0]) == [6,2,3,0,1,4,5]