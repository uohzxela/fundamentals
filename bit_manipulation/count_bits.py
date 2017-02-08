def count_bits(x):
	count = 0
	# number of iterations = number of bits in integer
	while x:
		count += x & 1
		x >>= 1
	return count

assert count_bits(0b11) == 2
assert count_bits(0b01) == 1
assert count_bits(0b1010) == 2
assert count_bits(0b1111) == 4

# version 2: drop lowest set bit to improve perf in best & avg cases
def count_bits2(x):
	count = 0
	# number of iterations = number of set bits
	while x:
		count += 1
		x &= x - 1
	return count

assert count_bits2(0b11) == 2
assert count_bits2(0b01) == 1
assert count_bits2(0b1010) == 2
assert count_bits2(0b1111) == 4
