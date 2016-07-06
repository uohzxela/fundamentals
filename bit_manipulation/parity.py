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
def parity3(x):
	x ^= x >> 32
	x ^= x >> 16
	x ^= x >> 8
	x ^= x >> 4
	x ^= x >> 2
	x ^= x >> 1
	return x & 1

assert parity(0x1011) == 1
assert parity(0x101) == 0
assert parity2(0x1011) == 1
assert parity2(0x101) == 0
assert parity3(0x1011) == 1
assert parity3(0x101) == 0
