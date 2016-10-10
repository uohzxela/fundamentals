def generate_matched_parens(n):
	res = []
	generate("", n, n, res)
	return res

def generate(s, left, right, res):
	if left == 0 and right == 0:
		res.append(s)
		return
	if left > 0:
		generate(s + "(", left-1, right, res)
	if left < right:
		generate(s + ")", left, right-1, res)

print generate_matched_parens(4)