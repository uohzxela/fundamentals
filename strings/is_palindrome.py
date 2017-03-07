def is_palindrome(s):
	"""
	Function which takes as input a string and returns true
	if that string is a palindromic string.

	Args:
		s (str): Input string.

	Returns:
		bool: Returns true if s is palindromic string, otherwise False.
	"""
	left = 0
	right = len(s) - 1
	while left < right:
		while not s[left].isalnum():
			left += 1
		while not s[right].isalnum():
			right -= 1
		if s[left].lower() != s[right].lower():
			return False
		left += 1
		right -= 1
	return True

assert is_palindrome("A man, a plan, a canal, Panama")
assert is_palindrome("Able was I, ere I saw Elba!")
assert is_palindrome("Nun123 321Nun")
assert not is_palindrome("Ray a Ray")