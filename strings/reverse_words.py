def reverse_words(words):
	A = list(words)
	A.reverse()
	i = 0
	while i < len(A):
		s = i
		while i < len(A) and A[i] != ' ':
			i += 1
		reverse_range(A, s, i-1)
		while i < len(A) and A[i] == ' ':
			i += 1
	return "".join(A)

def reverse_range(A, s, e):
	while s < e:
		A[s], A[e] = A[e], A[s]
		s += 1; e -= 1

assert reverse_words("Alice likes Bob") == "Bob likes Alice"
assert reverse_words("ram is costly") == "costly is ram"
assert reverse_words("my name is  Alex11") == "Alex11  is name my"
