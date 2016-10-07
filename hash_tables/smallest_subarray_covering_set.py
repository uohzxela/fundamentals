from collections import defaultdict

def find_smallest_subarray_covering_set(A, set):
	ht = {}
	for word in set:
		ht[word] = 0
	s = e = i = j = found = 0
	res = float('inf')
	while e < len(A):
		if A[e] in ht:
			if ht[A[e]] == 0:
				found += 1
			ht[A[e]] += 1
		while found == len(set):
			if e - s < res:
				res = e-s
				i, j = s, e
			if A[s] in ht: 
				ht[A[s]] -= 1
				if ht[A[s]] == 0:
					found -= 1
			s += 1
		e += 1
	return i, j

def find_smallest_subarray2(A, keywords):
	ht = defaultdict(int)
	for word in keywords:
		ht[word] += 1
	res = -1, -1
	remaining_to_cover = len(keywords)
	left = right = 0
	while right < len(A):
		if A[right] in ht:
			ht[A[right]] -= 1
			if ht[A[right]] >= 0:
				remaining_to_cover -= 1
		while remaining_to_cover == 0:
			i, j = res
			if (i == -1 and j == -1) or right - left < j - i:
				res = left, right
			if A[left] in ht:
				ht[A[left]] += 1
				if ht[A[left]] > 0:
					remaining_to_cover += 1
			left += 1
		right += 1
	return res

assert find_smallest_subarray_covering_set(
	"hello can you save the long long fat fat union but please just save save save the union please".split(), 
	['union', 'save']) == (15, 17)
assert find_smallest_subarray_covering_set(
	"hello can you save the long long fat fat union but please just save save save the union please".split(), 
	['fat', 'long']) == (6, 7)
assert find_smallest_subarray_covering_set(
	"apple banana apple apple dog cat apple dog banana apple cat dog".split(), 
	['banana', 'cat']) == (8, 10)

assert find_smallest_subarray2(
	"hello can you save the long long fat fat union but please just save save save the union please".split(), 
	['union', 'save']) == (15, 17)
assert find_smallest_subarray2(
	"hello can you save the long long fat fat union but please just save save save the union please".split(), 
	['fat', 'long']) == (6, 7)
assert find_smallest_subarray2(
	"apple banana apple apple dog cat apple dog banana apple cat dog".split(), 
	['banana', 'cat']) == (8, 10)