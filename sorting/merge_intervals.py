class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        res = []
        
        for interval in intervals:
            if res and res[-1].end >= interval.start:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res
