from swap_bits import swap

# brute-force approach
# assumption: word size is 8 bit long
def reverse_bits(x):
	NUM_BITS = 8
	for i in xrange(NUM_BITS/2):
		x = swap(x, NUM_BITS-i-1, i)
	return x

# assuming cache holds precomputed reversed word of size 16 bits
def reverse_bits_optimized(x, cache):
	WORD_SIZE = 16
	BIT_MASK = 0xFFFF
	return (cache[(x >> (3*WORD_SIZE)) & BIT_MASK] |
		   cache[(x >> (2*WORD_SIZE)) & BIT_MASK] << WORD_SIZE |
		   cache[(x >> WORD_SIZE) & BIT_MASK] << (WORD_SIZE * 2) |
		   cache[x & BIT_MASK] << (WORD_SIZE * 3))

assert reverse_bits(0b11110000) == 0b1111