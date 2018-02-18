class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for left in xrange(len(nums)):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                s = nums[left] + nums[mid] + nums[right]
                if s < 0:
                    mid += 1
                elif s > 0:
                    right -= 1
                else: # s == 0
                    res.append([nums[left], nums[mid], nums[right]])
                    while mid + 1 < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    mid += 1
                    while right - 1 > mid and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
        return res
