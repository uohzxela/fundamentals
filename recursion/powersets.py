# O(2^n)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subsets_(nums, 0, [], res)
        return res
    
    def subsets_(self, nums, i, partial, res):
        if i > len(nums)-1:
            res.append(list(partial))
            return
        
        partial.append(nums[i])
        self.subsets_(nums, i+1, partial, res)
        partial.pop()
        self.subsets_(nums, i+1, partial, res)