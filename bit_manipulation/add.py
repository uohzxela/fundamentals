def add(x, y):
	mask = 1
	x_copy = x
	y_copy = y
	res = carry = 0
	while x_copy or y_copy:
		x_bit = mask & x
		y_bit = mask & y
		res |= x_bit ^ y_bit ^ carry
		carry = (x_bit & y_bit) | (x_bit & carry) | (y_bit & carry)
		carry <<= 1
		mask <<= 1
		x_copy >>= 1
		y_copy >>= 1
	return res | carry

assert add(3, 6) == 9
assert add(3, 3) == 6
assert add(1, 2) == 3
assert add(10, 52) == 62
assert add(3, 7) == 10
