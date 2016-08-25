def replace_and_remove(A, size):
	"""
	Program which takes as input an array of characters, 
	and remove each 'b' and replaces each 'a' by two 'd's.
	Assume that there is enough space in the array to hold the final result.
	Args:
		A (list): An array of characters.
		size (int): Number of entries of the array that the operation is to be applied to.

	Returns:
		None (array modified in-place).
	"""
	write_idx = 0
	a_count = 0
	# forward iteration to remove 'b's and count the number of 'a's
	for i in xrange(size):
		if A[i] != 'b':
			A[write_idx] = A[i]
			write_idx += 1
		if A[i] == 'a':
			a_count += 1

	cur_idx = write_idx - 1
	write_idx = write_idx - 1 + a_count
	# backward iteration to replace 'a's with 'dd's starting from the end
	for i in xrange(cur_idx, -1, -1):
		if A[i] == 'a':
			A[write_idx] = 'd'
			write_idx -= 1
			A[write_idx] = 'd'
		else:
			A[write_idx] = A[i]
		write_idx -= 1

A = ['a', 'b', 'a', 'c', '']
replace_and_remove(A, 4)
assert A == ['d', 'd', 'd', 'd', 'c']

A = ['a', 'c', 'a', 'a', '', '', '']
replace_and_remove(A, 4)
assert A == ['d', 'd', 'c', 'd', 'd', 'd', 'd']

A = ['a', 'c', 'd', 'b', 'b', 'c', 'a']
replace_and_remove(A, 7)
assert A == ['d', 'd', 'c', 'd', 'c', 'd', 'd']
