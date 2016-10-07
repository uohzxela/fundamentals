def longest_contained_interval(A):
	res = 0
	ht = {}
	for num in A:
		if num in ht: continue
		interval_size = 1
		if num-1 in ht and num+1 in ht:
			interval_size = 1 + ht[num-1] + ht[num+1]
			ht[num - ht[num-1]] = interval_size
			ht[num + ht[num+1]] = interval_size
		elif num-1 in ht:
			interval_size = 1 + ht[num-1]
			ht[num-ht[num-1]] = interval_size
		elif num+1 in ht:
			interval_size = 1 + ht[num+1]
			ht[num+ht[num+1]] = interval_size
		ht[num] = interval_size
		res = max(interval_size, res)
	return res

assert longest_contained_interval([3,-2,7,9,8,1,2,0,-1,5,8]) == 6
assert longest_contained_interval([10,5,3,11,6,100,4]) == 4