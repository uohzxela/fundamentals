def find_duplicate_and_missing(A):
	# compute the XOR of all numbers from 0 to len(A)-1 and all entries in A
	miss_XOR_dup = 0
	for i in xrange(len(A)):
		miss_XOR_dup ^= i ^ A[i]

	# sets all bits in diff_bit to 0 
	# except for the least significant bit that's set to 1
	diff_bit = miss_XOR_dup & (~(miss_XOR_dup - 1))

	miss_OR_dup = 0
	for i in xrange(len(A)):
		# focus on entries or numbers in which the diff_bit-th bit is 1
		if i & diff_bit != 0:
			miss_OR_dup ^= i
		if A[i] & diff_bit != 0:
			miss_OR_dup ^= A[i]

	# miss_OR_dup is either the missing value or the duplicated entry
	if miss_OR_dup in A:
		# miss_OR_dup is the duplicate
		return miss_OR_dup, miss_OR_dup ^ miss_XOR_dup 
	else:
		# miss_OR_dup is the missing value
		return miss_OR_dup ^ miss_XOR_dup, miss_OR_dup

assert find_duplicate_and_missing([5,3,0,3,1,2]) == (3, 4)
assert find_duplicate_and_missing([4,1,0,3,4,2]) == (4, 5)
assert find_duplicate_and_missing([5,1,0,3,5,2]) == (5, 4)
assert find_duplicate_and_missing([0,1,0,3,4,2]) == (0, 5)
