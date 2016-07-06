NUM_UNSIGNED_BITS = 63
def closest(x):
	for i in xrange(NUM_UNSIGNED_BITS-1):
		if (x >> i) & 1 != (x >> i+1) & 1:
			x ^= (1 << i | 1 << i+1)
			return x
	raise Exception("All bits are 0 or 1.")


assert closest(7) == 11
assert closest(6) == 5
