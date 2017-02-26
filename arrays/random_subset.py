from collections import defaultdict
from random import randint

def random_subset(n, k):
	changed = defaultdict(lambda: None)
	for i in xrange(k):
		rand_idx = randint(i, n-1)
		p1 = changed[rand_idx]
		p2 = changed[i]
		if p1 is None and p2 is None:
			changed[i] = rand_idx
			changed[rand_idx] = i
		elif p1 is None and p2 is not None:
			changed[i] = rand_idx
			changed[rand_idx] = p2
		elif p1 is not None and p2 is None:
			changed[i] = p1
			changed[rand_idx] = i
		else:
			changed[i] = p1
			changed[rand_idx] = p2
	res = []
	for i in xrange(k):
		res.append(changed[i])
	return res

print random_subset(100, 4)