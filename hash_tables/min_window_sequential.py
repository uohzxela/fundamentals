def min_window_sequential(paragraph, keywords):
	'''
	Write a program that takes two arrays of strings, and return the indices of the starting and ending
	index of a shortest subarray of the first array (paragraph array) that sequentially covers all the strings
	in the second array (keywords array), in the order in which they appear in the keywords array.

	Assume all keywords are distinct.
	'''
	keyword_to_idx = { k: i for i, k in enumerate(keywords) }
	latest_occurrence = [-1] * len(keywords)
	shortest_subarray_length = [float('inf')] * len(keywords)
	res = [-1, -1]
	shortest_dist = float('inf')

	for i, word in enumerate(paragraph):
		if word in keyword_to_idx:
			keyword_idx = keyword_to_idx[word]
			if keyword_idx == 0:
				shortest_subarray_length[keyword_idx] = 1
			elif shortest_subarray_length[keyword_idx-1] != float('inf'):
				dist_to_previous = i - latest_occurrence[keyword_idx-1]
				shortest_subarray_length[keyword_idx] = dist_to_previous + shortest_subarray_length[keyword_idx-1]

			latest_occurrence[keyword_idx] = i

			if keyword_idx == len(keywords)-1 and shortest_subarray_length[-1] < shortest_dist:
				shortest_dist = shortest_subarray_length[-1]
				res = [latest_occurrence[0], i]
	return res

assert min_window_sequential(
	['apple', 'banana', 'cat', 'dog', 'banana', 'alex', 'apple'],
	['banana', 'apple']) == [4, 6]
