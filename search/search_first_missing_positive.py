class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                j = nums[i]-1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for j in xrange(len(nums)):
            if nums[j] != j+1:
                return j+1
        return len(nums)+1


Solution().firstMissingPositive([2,1])