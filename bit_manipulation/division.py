"""
1. compute largest k such that (2^k)y <= x
2. subtract (2^k)y from x
3. add 2^k to the quotient
4. repeat until x < y
"""
def division(x, y):
	power = 32
	y_power = y << power
	res = 0
	while x >= y:
		while y_power > x:
			y_power >>= 1
			power -= 1
		res += (1 << power)
		x -= y_power
	return res 

assert division(12, 3) == 4
assert division(123, 4) == 30
assert division(2, 2) == 1