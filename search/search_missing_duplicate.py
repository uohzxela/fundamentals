'''
MISSING:
if len(A) == n-1, and 1 <= A[i] <=n
	1. sum up all numbers from 1 to n, substract A[i] from sum to find missing
	2. XOR all numbers from 1 to n, XOR all numbers in A, then XOR both to get the missing
else
	use bucket sort, find the first missing element in second pass (A[i] != i)
DUPLICATE:
if len(A) == n+1, and 1 <= A[i] <= n
	1. sum up all numbers from 1 to n, sum up all numbers in A, substract A - first sum to get duplicate
	2. same XOR method as above
else
	use bucket sort, stop when duplicate element is found (A[A[currIndex]] == A[currIndex] and A[currIndex] != currIndex)
'''