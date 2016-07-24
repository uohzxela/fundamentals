import math

def is_palindrome_number(x):
	if x < 0: return False
	if x == 0: return True
	num_digits = int(math.log(x, 10)) + 1
	msb_mask = pow(10, num_digits-1)
	for i in xrange(num_digits/2):
		if x / msb_mask != x % 10:
			return False
		x %= msb_mask
		x /= 10
		msb_mask /= 100
	return True

assert is_palindrome_number(12321)
assert is_palindrome_number(-123) == False
assert is_palindrome_number(0)
assert is_palindrome_number(45644654)
