def reverse_words(words):
	A = list(words)
	reverse(A, 0, len(A)-1)
	i = 0
	while i < len(A):
		s = i
		while i < len(A) and A[i] != ' ':
			i += 1
		reverse(A, s, i-1)
		while i < len(A) and A[i] == ' ':
			i += 1
	return "".join(A)

def reverse(A, s, e):
	for i in xrange((e-s+1)/2):
		A[s+i], A[e-i] = A[e-i], A[s+i]

assert reverse_words("Alice likes Bob") == "Bob likes Alice"
assert reverse_words("ram is costly") == "costly is ram"
assert reverse_words("my name is  Alex11") == "Alex11  is name my"
