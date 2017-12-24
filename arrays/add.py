def add(A, B):
	res = []
	i, j = len(A)-1, len(B)-1
	curr = 0
	while i >= 0 or j >= 0:
		if i >= 0:
			curr += A[i]
		if j >= 0:
			curr += B[i]
		res.append(curr % 10)
		curr /= 10
		i, j = i - 1, j - 1
	if curr > 0:
		res.append(curr)
	res.reverse()
	return res

assert add([9,9], [9,9]) == [1, 9, 8]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
