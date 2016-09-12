class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            n = nums[i]
            if n > 0 and n <= len(nums) and nums[n-1] != n:
                nums[i], nums[n-1] = nums[n-1], nums[i]
                continue
            i += 1
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums)+1


Solution().firstMissingPositive([2,1])