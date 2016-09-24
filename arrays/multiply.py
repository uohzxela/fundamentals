"""
similar to strings/multiply_bigint.py
"""
def multiply(A, B):
	sign = -1 if A[0] < 0 or B[0] < 0 else 1
	A[0] = abs(A[0])
	B[0] = abs(B[0])
	A.reverse()
	B.reverse()
	res = [0] * (len(A) + len(B))
	for i in xrange(len(A)):
		carry = 0
		for j in xrange(len(B)):
			res[i+j] += carry + (A[i] * B[j])
			carry = res[i+j]/10
			res[i+j] %= 10
		res[i+len(B)] += carry
	if res[-1] == 0: res = res[:-1]
	res.reverse()
	res[0] *= sign
	return res

assert multiply([9,9], [-9,9]) == [-9,8,0,1]
assert multiply([9,9], [9,9]) == [9,8,0,1]
assert multiply([1,9,3,7,0,7,7,2,1], [-7,6,1,8,3,8,2,5,7,2,8,7]) == [-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7]
