def reverse_digits(x):
	x_tmp, res = abs(x), 0
	while x_tmp:
		res = res * 10 + x_tmp % 10
		x_tmp /= 10
	return -res if x < 0 else res

assert reverse_digits(-123) == -321
assert reverse_digits(4522) == 2254
assert reverse_digits(1) == 1
