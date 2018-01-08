# this solution is really about finding floor(sqrt(x)) so we need to return (left - 1)
def sqrt(x):
    left, right = 0, x
    while left <= right:
        mid = (left + right)/2
        if mid*mid <= x:
            left = mid + 1
        else:
            right = mid - 1
    # why minus 1? because left = mid + 1,
    # we need to return the most recent mid
    return left - 1

assert sqrt(0) == 0
assert sqrt(1) == 1
assert sqrt(4) == 2
assert sqrt(9) == 3
assert sqrt(300) == 17
assert sqrt(25) == 5

# alternative solution
# easier to remember since it uses the same trick as searching for first occurrence of k
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s, e = 0, x
        res = 0
        while s <= e:
            m = (s + e)/2
            mm = m * m
            if mm == x:
                return m
            elif mm < x:
                s = m + 1
                res = m # this is the trick
            else:
                e = m - 1
                # if search for first ocurrrence, res = m would be set here
        return res
