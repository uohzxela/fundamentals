def search_entry_equal_to_index(A):
	s, e = 0 , len(A) - 1
	while s <= e:
		m = (s + e) / 2
		if A[m] == m:
			return m
		elif A[m] < m:
			s = m + 1
		else:
			e = m - 1
	return -1

A = [-2, 0, 2, 3, 6, 7, 9]
assert search_entry_equal_to_index(A) == 3
