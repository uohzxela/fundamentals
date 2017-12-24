def plus_one(A):
	carry = 1
	for i in xrange(len(A)-1, -1, -1):
		A[i] += carry
		carry = A[i] / 10
		A[i] %= 10
		if carry == 0:
			break
	if carry > 0:
		A[0] = 1
		A.append(0)
	return A

assert plus_one([9,9]) == [1,0,0]
assert plus_one([1,2,9]) == [1,3,0]
assert plus_one([9]) == [1,0]
assert plus_one([9,9,9,9]) == [1,0,0,0,0]
