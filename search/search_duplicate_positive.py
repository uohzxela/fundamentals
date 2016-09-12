class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            n = nums[i]
            if n > 0 and n <= len(nums):
                if nums[n-1] != n:
                    nums[n-1], nums[i] = nums[i], nums[n-1]
                    continue
                elif nums[n-1] == n and i != n-1:
                    return n
            i += 1
        return -1