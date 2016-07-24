def division(x, y):
	power = 32
	yPower = y << power
	res = 0
	while x >= y:
		while yPower > x:
			yPower >>= 1
			power -= 1
		res += (1 << power)
		x -= yPower
	return res 

assert division(12, 3) == 4
assert division(123, 4) == 30
assert division(2, 2) == 1