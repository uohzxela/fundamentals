from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heappush(self.max_heap, -heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

        # alternative version
        # heappush(self.min_heap, -heappushpop(self.max_heap, -num))
        # if len(self.max_heap) < len(self.min_heap):
        #     heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (self.min_heap[0] + (-self.max_heap[0]))
        else:
            return float(self.min_heap[0])

        # alternative version
        # if len(self.min_heap) == len(self.max_heap):
        #     return 0.5 * (self.min_heap[0] + (-self.max_heap[0]))
        # else:
        #     return float(-self.max_heap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
