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
	BASE_TEN = 10
	decimal = 0
	is_neg = s[0] == '-'
	for c in s:
		if c.isalpha():
			decimal = b1 * decimal + BASE_TEN + ord(c) - ord('A')
		elif c.isdigit():
			decimal = b1 * decimal + ord(c) - ord('0')

	res = []
	while decimal:
		d = decimal % b2
		if d >= BASE_TEN:
			c = chr(ord('A') + d - BASE_TEN)
		else:
			c = chr(ord('0') + d)
		res.append(c)
		decimal /= b2

	if is_neg: res.append('-')
	res.reverse()
	
	return ''.join(res)

assert convert_base("1A7", 13, 7) == "615"
assert convert_base("-1A7", 13, 7) == "-615"
assert convert_base("615", 7, 13) == "1A7"