def swap(x, i, j):
	# extract i-th and j-th bits, see if they differ
	if (x >> i) & 1 != (x >>j) & 1:
		x ^= ( 1 << i | 1 << j ) # flip i-th and j-th bits using XOR
	return x

assert swap(73, 1, 6) == 11