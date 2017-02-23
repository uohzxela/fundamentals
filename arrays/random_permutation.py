from offline_sampling import offline_sampling

def random_permutation(n):
	permutation = [x for x in xrange(n)]
	return offline_sampling(permutation, n)

print random_permutation(10)
