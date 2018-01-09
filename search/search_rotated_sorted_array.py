class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s, e = 0, len(nums)-1
        while s <= e:
            m = (s+e)/2
            if nums[m] == target:
                return m
            # is left side sorted?
            if nums[s] <= nums[m]:
                # is target in left side?
                if nums[s] <= target < nums[m]:
                    e = m-1
                else:
                    s = m+1
            # if not, right side is sorted
            else:
                # is target in right side?
                if nums[m] < target <= nums[e]:
                    s = m+1
                else:
                    e = m-1
        return -1
