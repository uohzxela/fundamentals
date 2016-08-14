def convert_base(s, b1, b2):
	"""
	Program that performs base conversion.

	Args:
		s (str): The string which represents an integer in base1.
		b1 (int): base1.
		b2 (int): base2.

	Returns:
		Output should be the string representing the integer in base2.
	"""
	x = 0
	is_neg = s[0] == '-'
	for c in s:
		if c.isalpha():
			x = b1 * x + 10 + ord(c) - ord('A')
		elif c.isdigit():
			x = b1 * x + ord(c) - ord('0')

	res = []
	while x:
		mod = x % b2
		if mod >= 10:
			mod = chr(ord('A') + mod - 10)
		else:
			mod = str(mod)
		res.append(mod)
		x /= b2

	if is_neg: res.append('-')
	res.reverse()
	
	return ''.join(res)

assert convert_base("1A7", 13, 7) == "615"
assert convert_base("-1A7", 13, 7) == "-615"
assert convert_base("615", 7, 13) == "1A7"