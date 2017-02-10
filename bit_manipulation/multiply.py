from add import add

def multiply(x, y):
	res = 0
	while y:
		if y & 1:
			res = add(res, x)
		y >>= 1
		x <<= 1
	return res

assert multiply(2, 3) == 6
assert multiply(2, 4) == 8
assert multiply(7, 8) == 56
assert multiply(3, 11) == 33
assert multiply(10, 12) == 120
