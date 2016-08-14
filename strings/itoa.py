def itoa(n):
	s = []
	isNeg = False
	if n < 0:
		isNeg = True
		n = abs(n)
	while n:
		c = n % 10
		s.append(chr(c + ord('0')))
		n /= 10
	if isNeg: s.append('-')
	s.reverse()
	return ''.join(s)

assert itoa(3459210) == '3459210'
assert itoa(-123349) == '-123349'