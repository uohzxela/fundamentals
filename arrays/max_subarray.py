def maxSubarray(A):
	currSum = A[0]
	maxSum = 0
	for i in xrange(1,len(A)):
		maxSum = max(currSum, maxSum)
		currSum += A[i]
		if currSum < 0: currSum = 0

	return maxSum

print maxSubarray([-2,1,-3,4,-1,2,1,-5,4])