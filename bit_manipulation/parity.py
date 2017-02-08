# O(n) where n = word size
def parity(x):
	res = 0
	while x:
		res ^= (x & 1)
		x >>= 1
	return res

# O(k) where k = number of bits set to 1 in word
def parity2(x):
	res = 0
	while x:
		res ^= 1 
		x &= (x-1) # drops lowest set bit
	return res

# O(logn) where n = word size
# assumption: x is 64 bit long
def parity3(x):
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1
	return x & 1

# O(n/L), where n = 64, and L = 16
# another solution: use precomputed cache of size 2^16,
# each cache slot holds the parity of 16-bit word
def parity_cache(x, cache):
	WORD_SIZE = 16
	# masks 16 least-significant bits
	BIT_MASK = 0xFFFF
	return (cache[x & BIT_MASK] ^
		   cache[(x >> WORD_SIZE) & BIT_MASK] ^
		   cache[(x >> (WORD_SIZE * 2)) & BIT_MASK] ^
		   cache[(x >> (WORD_SIZE * 3)) & BIT_MASK])

assert parity(0x1011) == 1
assert parity(0x101) == 0
assert parity2(0x1011) == 1
assert parity2(0x101) == 0
assert parity3(0x1011) == 1
assert parity3(0x101) == 0
