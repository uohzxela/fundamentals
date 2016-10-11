def palin_decomp(s):
	decompose(s, [], 0, 0)

def is_palindromic(s, l, r):
	while l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

def decompose(s, decompositions, l, r):
	if r == len(s):
		if l == r:
			print decompositions
		return
	if is_palindromic(s, l, r):
		decompositions.append(s[l:r+1])
		decompose(s, decompositions, r+1, r+1)
		decompositions.pop()
	decompose(s, decompositions, l, r+1)


# palin_decomp("aab")
palin_decomp('0204451881')