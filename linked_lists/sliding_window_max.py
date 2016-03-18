from Queue import deque 
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        q = []
        for i in xrange(k):
        	while q and nums[q[-1]] <= nums[i]:
        		q.pop()
        	q.append(i)
        res = []
        for i in xrange(k, len(nums)):
        	res.append(nums[q[0]])
        	while q and nums[q[-1]] <= nums[i]:
        		q.pop()
        	while q and q[0] <= i-k:
        		q.pop(0)
        	q.append(i)
        res.append(nums[q[0]])
        return res

print Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)