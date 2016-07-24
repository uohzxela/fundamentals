def reverse_bits(x):
	WORD_SIZE = 16
	BIT_MASK = 0xFFFF
	return cache[(x >> (3*WORD_SIZE)) & BIT_MASK] |
		   cache[(x >> (2*WORD_SIZE)) & BIT_MASK] << WORD_SIZE |
		   cache[(x >> WORD_SIZE) & BIT_MASK] << (WORD_SIZE * 2) |
		   cache[x & BIT_MASK] << (WORD_SIZE * 3)