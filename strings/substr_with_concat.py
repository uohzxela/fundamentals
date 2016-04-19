'''
start by looping over 0..j..k
    right = left = j
    clear substrCounter
    while right < len(s) - k +1:
        substr = s[right:right+k]
        if substr in counter:
            increase substrCounter[substr] by 1
            while substrCounter[substr] > counter[substr]:
                chop off left substrings of size k
                move left index by k to right
            if substrCounter is equal to counter:
                add left index to result
                chop off 1 left substring of size k
                move left index by k to the right
        else:
            clear substrCounter
            shift left index by k to the right
'''


from collections import Counter, defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        counter = Counter(words)
        substrCounter = defaultdict(int)
        k = len(words[0])
        start = i = 0
        res = []
        for j in xrange(k):
            i = j
            start = j
            substrCounter.clear()
            while i < len(s)-k+1:
                substr = s[i:i+k]
                if substr in counter:
                    substrCounter[substr] += 1
                    while substrCounter[substr] > counter[substr]:
                        substrCounter[s[start:start+k]] -= 1
                        start += k
                    if substrCounter == counter: 
                        res.append(start)
                        substrCounter[s[start:start+k]] -= 1
                        start += k
                else:
                    substrCounter.clear()
                    start = i + k
                i += k

        return res


print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
print Solution().findSubstring("dogthecatcatthedog", ["cat", "the"])
print Solution().findSubstring("aaaaaaaa", ["aa", "aa", "aa"])
print Solution().findSubstring("ababaab", ["ab", "ba", "ba"])