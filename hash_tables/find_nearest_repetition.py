def find_nearest_repetition(A):
	ht = {}
	nearest_dist = float("inf")
	for i, word in enumerate(A.split(" ")):
		if word in ht:
			nearest_dist = min(nearest_dist, i - ht[word])
		ht[word] = i
	return nearest_dist

assert find_nearest_repetition("All work and no play makes for no work no fun and no results") == 2