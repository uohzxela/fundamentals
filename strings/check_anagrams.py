from collections import defaultdict
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
        for k,v in count.iteritems():
            if v != 0: return False
        return True