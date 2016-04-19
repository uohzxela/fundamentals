def genParens(n):
	parens("", n, n)

def parens(s, left, right):
	if left == 0 and right == 0:
		print s
		return
	if left > 0:
		parens(s + "(", left-1, right)
	if left < right:
		parens(s + ")", left, right-1)

genParens(4)