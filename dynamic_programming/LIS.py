# brute force recursive
# T = O(2^n), use { 1,2,3,4,5 ... } as worst case = # of possible subsequences
# def lis(arr):
# 	max = 0
# 	n = len(arr)
# 	for i in xrange(n):
# 		ans1 = lis_(i, n, arr)
# 		if ans1 > max: max = ans1
# 	return max

# def lis_(i, n, arr):
# 	if (i == n-1): return 1
# 	max = 0
# 	for j in xrange(i+1, n):
# 		if arr[i] < arr[j]:
# 			ans1 = lis_(j, n, arr)
# 			if ans1 > max: max = ans1
# 	return max+1


# recursion with cache, memoization
# def lis(arr):
# 	max = 0
# 	n = len(arr)
# 	lis_cache = [None]*n 
	
# 	for i in xrange(n):
# 		ans1 = lis_(i, n, arr, lis_cache)
# 		if ans1 > max: max = ans1
# 	return max

# def lis_(i, n, arr, lis_cache):
# 	if lis_cache[i] is None:
# 		if (i == n-1): lis_cache[i] = 1
# 		max = 0
# 		for j in xrange(i+1, n):
# 			if arr[i] < arr[j]:
# 				ans1 = lis_(j, n, arr, lis_cache)
# 				if ans1 > max: max = ans1
# 		lis_cache[i] = max+1
# 	return lis_cache[i]

# iterative
def lis(arr):
	max = 0
	n = len(arr)
	lis_cache = [None]*n 
	for i in xrange(n-1, -1, -1):
		max = 0
		for j in xrange(i+1, n):
			if arr[i] < arr[j] and lis_cache[j] > max:
				max = lis_cache[j]
		lis_cache[i] = max+1
	for i in xrange(n):
		if lis_cache[i] > max: max = lis_cache[i]
	return max

arr = [-7, 10, 9, 2, 3, 8, 8, 1]
print lis(arr)