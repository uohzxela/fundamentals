import random

def offline_sampling(A, k):
	for i in xrange(k):
		# generate a random int in [i, len(A)-1]
		target = random.randint(i, len(A)-1)
		A[i], A[target] = A[target], A[i]
	return A

# print offline_sampling([1,2,3,4,5,6,7,8], 5)
