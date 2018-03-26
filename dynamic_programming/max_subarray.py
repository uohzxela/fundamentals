# compare with arrays/max_subarray_product.py (similar solution)
# can handle all negative numbers too
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = global_max = nums[0]
        for num in nums[1:]:
            local_max = max(local_max + num, num)
            global_max = max(local_max, global_max)
        return global_max
