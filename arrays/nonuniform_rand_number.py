import random

def bsearch(prefix, k):
	s, e = 0, len(prefix)-1
	while s <= e:
		m = (s+e)/2
		if prefix[m] <= k:
			if k <= prefix[m+1]:
				return m
			else:
				s = m+1
		else:
			e = m-1
	return -1

def nonuniform_rand_number(values, probabilities):
	prefix = [0.]
	for p in probabilities:
		prefix.append(prefix[-1] + p)
	rand = random.uniform(0, 1)
	return values[bsearch(prefix, rand)]

def test():
	count3 = 0
	count11 = 0
	for i in xrange(18):
		num = nonuniform_rand_number([3,5,7,11],[9./18,6./18,2./18,1./18])
		# most probable
		if num == 3:
			count3 += 1
		# least probable
		elif num == 11:
			count11 += 1
	print "occurrence of least probable number(11):", count11/18.
	print "occurrence of most probable number(3):", count3/18.

test()
