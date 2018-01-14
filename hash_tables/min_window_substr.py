import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left,  = 0
        tmap = collections.Counter(t)
        remaining = len(tmap)
        min_len = float('inf')
        res = ""

        for right in xrange(len(s)):
            c = s[right]
            if c in tmap:
                tmap[c] -= 1
                if tmap[c] == 0:
                    remaining -= 1
            while remaining == 0:
                c = s[left]
                if c in tmap:
                    tmap[c] += 1
                    if tmap[c] > 0:
                        remaining += 1
                if right - left + 1 < min_len:
                    res = s[left:right+1]
                    min_len = right - left + 1
                left += 1
        return res
