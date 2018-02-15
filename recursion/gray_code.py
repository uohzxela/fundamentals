class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def helper(n):
            if not n:
                return ['0']
            if n == 1:
                return ['0', '1']
            partials = helper(n - 1)
            return (map(lambda x: '0' + x, partials) +
                    map(lambda x: '1' + x, reversed(partials)))

        return map(lambda x: int(x, 2), helper(n))
