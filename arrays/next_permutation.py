class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		# 1. from right to left, find the first digit which violates the increasing property (partitionDigit)
		# 2. from right to left, find the first digit > than partitionDigit (changeDigit)
		# 3. swap changeDigit and partitionDigit
		# 4. reverse all digits to the right of partitionIndex

		n = len(nums)
		partitionIndex = -1
		for i in xrange(n-2, -1, -1):
			if nums[i] < nums[i+1]:
				partitionIndex = i
				break
		if partitionIndex == -1:
			nums.reverse()
			return
		partitionDigit = nums[partitionIndex]
		changeIndex = 0
# 		for i in xrange(n-1, -1, -1):
# 			if nums[i] > partitionDigit:
# 				changeIndex = i
# 				break
		changeIndex = self.search(nums, partitionIndex+1, len(nums)-1, partitionDigit)
		nums[partitionIndex], nums[changeIndex] = nums[changeIndex], nums[partitionIndex]
		self.reverse(nums, partitionIndex+1)
	def search(self, nums, s, e, k):
		while s <= e:
			m = (s+e)/2
			if (m==e) or (nums[m] > k and m+1 <= e and nums[m+1] <= k):
				return m
			elif nums[m] > k:
				s = m+1
			else:
				e = m-1
	def reverse(self, nums, p):
		n = len(nums)
		for i in xrange(p, (p+n)/2):
			nums[i], nums[n+p-1-i] = nums[n+p-1-i], nums[i]


Solution().nextPermutation([1,3,2])