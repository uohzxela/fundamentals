def pow(x, y):
	res = 1.0
	power = y
	if y < 0:
		power = -power # make it positive
		x = 1.0/x
	while power:
		if power & 1:
			res *= x
		x *= x
		power >>= 1
	return res

assert pow(2, 3) == 8
assert pow(2.0, -3) == 1.0/8
assert pow(2.0, 4) == 16