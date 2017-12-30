def atoi(s):
	s = s.strip()
	if not s:
		return 0
	res = 0
	sign = -1 if s[0] == '-' else 1
	start = 1 if not is_digit(s[0]) else 0
	for i in xrange(start, len(s)):
		if not is_digit(s[i]): 
			break
		res = res * 10 + (ord(s[i]) - ord('0'))
	return res * sign

def is_digit(c):
	return ord('0') <= ord(c) <= ord('9')

assert atoi("2147483648") == 2147483648
assert atoi("-123") == -123
assert atoi("+123") == 123
