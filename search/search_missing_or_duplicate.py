'''
MISSING:
if len(A) == n-1, and 1 <= A[i] <=n
	1. sum up all numbers from 1 to n, substract A[i] from 0 to n-1 from sum to find missing
	2. XOR all numbers from 1 to n, XOR all numbers in A, then XOR both to get the missing
else
	use bucket sort, find the first missing element in second pass (A[i] != i+1)
	see search_first_missing_positive.py for implementation of bucket sort (first loop)
DUPLICATE:
if len(A) == n+1, and 1 <= A[i] <= n
	1. sum up all numbers from 1 to n, sum up all numbers in A, substract A - first sum to get duplicate
	2. same XOR method as above
else
	use bucket sort, stop when duplicate element is found 
		let n = A[curr_index]
		stop when A[n-1] == n and n-1 != curr_index
'''

