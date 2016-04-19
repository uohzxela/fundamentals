def palinDecomp(s):
	palin(s, [], 0, 0)

def isPalin(s, l, r):
	while l < r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

def palin(s, curr, l, r):
	if r == len(s):
		if l == r: print curr
		return

	if isPalin(s, l, r):
		curr.append(s[l:r+1])
		palin(s, curr, r+1, r+1)
		curr.pop()
	palin(s, curr, l, r+1)


palinDecomp("aab")