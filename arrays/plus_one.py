def plus_one(A):
	A.reverse()
	carry = 1
	for i in xrange(len(A)):
		A[i] += carry
		carry = A[i] / 10
		A[i] %= 10
		if carry == 0: break
	if carry > 0:
		A.append(1)
	A.reverse()
	return A

assert plus_one([9,9]) == [1,0,0]
assert plus_one([1,2,9]) == [1,3,0]
assert plus_one([9]) == [1,0]
assert plus_one([9,9,9,9]) == [1,0,0,0,0]