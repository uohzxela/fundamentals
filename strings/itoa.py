def itoa(n):
	s = []
	while n:
		c = n % 10
		s.append(chr(c + ord('0')))
		n /= 10
	s.reverse()
	return ''.join(s)

print itoa(3459210)