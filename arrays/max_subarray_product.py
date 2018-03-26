class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = local_min = global_max = nums[0]
        for num in nums[1:]:
            if num > 0:
                local_max = max(local_max * num, num)
                local_min = min(local_min * num, num)
            else:
                local_max, local_min = max(local_min * num, num), min(local_max * num, num)
            global_max = max(local_max, global_max)
        return global_max
