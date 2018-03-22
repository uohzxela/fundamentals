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

"""
Try to grok this patterna and you will understand this solution.

0: 0000
1: 0001
2: 0010
3: 0011
...
8: 1000
9: 1001
...
12: 1100
13: 1101
14: 1110
15: 1111
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        for x in xrange(1, num+1):
            res.append(res[x >> 1] + (x & 1))
        return res
