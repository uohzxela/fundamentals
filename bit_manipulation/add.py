def add(a, b):
	tempA = a
	tempB = b
	sum = carryin = 0
	k = 1
	while tempA or tempB:
		ak = a & k
		bk = b & k 
		carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
		sum |= (ak ^ bk ^ carryin)
		tempA >>= 1
		tempB >>= 1
		k <<= 1
		carryin = carryout << 1
	return sum | carryin


assert add(1,2) == 3
assert add(10, 52) == 62
assert add(3, 7) == 10