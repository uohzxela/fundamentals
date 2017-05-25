# O(n!)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, 0, res)
        return res

    def helper(self, nums, k, res):
        if k == len(nums):
            res.append(list(nums))
            return
        for i in xrange(k, len(nums)):
            nums[i], nums[k] = nums[k], nums[i]
            self.helper(nums, k+1, res)
            nums[i], nums[k] = nums[k], nums[i]
