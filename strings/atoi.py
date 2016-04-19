def atoi(s):
	if not s: return 0
	res = 0
	s = s.strip()
	n = len(s)
	isNeg = s[0] == '-'
	start = 1 if isNeg or s[0] == '+' else 0
	for i in xrange(start, n):
		if ord(s[i]) < ord('0') or ord(s[i]) > ord('9') :  break
		res = res * 10 + (ord(s[i])- ord('0'))
	return -res if isNeg else res

print atoi("2147483648")