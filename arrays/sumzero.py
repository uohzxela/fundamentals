# Complete the function below.

def sumZero(A):
	ht = {}
	sum = 0
	res = []
	print A
	for i in xrange(len(A)):
		sum += A[i]
		if sum in ht:
			res.append(','.join(map(str, A[ht[sum]+1: i+1])))
			ht[sum] = i
		elif A[i] == 0:
			res.append('0')
			ht[0] = i
		else:
			ht[sum] = i
	return res


# print sumZero([5,1,2,-3,7,-4])
print sumZero([0,1,2,3,4,-10])