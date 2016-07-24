def reverse_digits(x):
	is_negative = x < 0
	x = abs(x)
	res = 0
	while x:
		res = res * 10 + x % 10
		x /= 10
	return -res if is_negative else res

assert reverse_digits(-123) == -321
assert reverse_digits(4522) == 2254
assert reverse_digits(1) == 1