# this solution is really about finding floor(sqrt(x))
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return x
        lo,hi = 0, x
        ans = 0
        while hi-lo >= 0:
            m = (hi+lo)/2
            if m*m == x: return m
            if m*m > x: 
                hi = m-1
            else:
                # Since we need floor, we update answer when mid*mid is
                # smaller than x, and move closer to sqrt(x)
                lo = m+1
                ans = m
        return ans
        