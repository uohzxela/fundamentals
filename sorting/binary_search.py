def binary_search(a, k):
	s, e = 0, len(a)-1
	while s <= e:
		m = (s+e)/2
		if a[m] < k:
			s = m + 1
		elif a[m] > k:
			e = m -1
		else:
			return m
	return -1


print binary_search([1,2,6,9,13,20], 20)