from add import add

def multiply(a, b):
	sum = 0
	while a:
		if a & 1:
			sum = add(sum, b)
		a >>= 1
		b <<= 1
	return sum

assert multiply(2, 3) == 6
assert multiply(2, 4) == 8
assert multiply(7, 8) == 56
assert multiply(3, 11) == 33
assert multiply(10, 12) == 120