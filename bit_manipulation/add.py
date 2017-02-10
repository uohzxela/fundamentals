def add(x, y):
	k = 1
	x_temp = x
	y_temp = y
	res = carry = 0
	while x_temp or y_temp:
		xk = k & x
		yk = k & y
		res |= xk ^ yk ^ carry
		carry = (xk & yk) | (xk & carry) | (yk & carry)
		carry <<= 1
		k <<= 1
		x_temp >>= 1
		y_temp >>= 1
	return res | carry

assert add(3, 6) == 9
assert add(3, 3) == 6
assert add(1, 2) == 3
assert add(10, 52) == 62
assert add(3, 7) == 10