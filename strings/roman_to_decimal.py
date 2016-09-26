def roman_to_decimal(s):
	T = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}
	# start from the back, if the current symbol violates
	# the nonincreasing property, decrease it from the decimal value
	decimal = T[s[-1]]
	for i in xrange(len(s)-2, -1, -1):
		if T[s[i]] < T[s[i+1]]:
			decimal -= T[s[i]]
		else:
			decimal += T[s[i]]
	return decimal

assert roman_to_decimal("IC") == 99
assert roman_to_decimal("LIX") == 59