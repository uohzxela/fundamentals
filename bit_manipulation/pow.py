# preferred approach as while loop avoids the overhead of function calls
def pow(x, y):
	res = 1.0
	power = y
	if y < 0:
		power = -power # make it positive
		x = 1.0/x # use float as numerator to avoid rounding to integer
	while power:
		# if power is odd
		if power & 1:
			res *= x
		x *= x
		power >>= 1
	return res

def pow2(x, y):
	if y < 0:
		return 1.0/pow2_(x, -y)
	return pow2_(x, y)

# same idea but uses recursion
def pow2_(x, y):
	if y == 0:
		return 1
	tmp = pow2_(x, y >> 1)
	if y & 1:
		return x * tmp * tmp
	else:
		return tmp * tmp

assert pow(2, 3) == 8
assert pow(2.0, -3) == 1.0/8
assert pow(2.0, 4) == 16

assert pow2(2, 3) == 8
assert pow2(2.0, -3) == 1.0/8
assert pow2(2.0, 4) == 16
