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

def binary_search_r(a, k):
	return binary_search_r_(a, 0, len(a)-1, k)

def binary_search_r_(a, s, e, k):
	if s > e: return -1
	m = (s+e)/2
	if a[m] == k:
		return m
	elif a[m] < k:
		return binary_search_r_(a, m+1, e, k)
	else:
		return binary_search_r_(a, s, m-1, k)


assert binary_search([1,2,6,9,13,20], 20) == 5
assert binary_search([1,2,6,9,13,20], 21) == -1

assert binary_search_r([1,2,6,9,13,20], 20) == 5
assert binary_search_r([1,2,6,9,13,20], 21) == -1
