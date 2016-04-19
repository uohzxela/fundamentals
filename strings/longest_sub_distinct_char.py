# only find substrings with 2 distinct chars
def  longestSub(s):
    hm = {}
    left = maxLen = 0
    res = ""
    for i in xrange(len(s)):
        c = s[i]
        if c not in hm: hm[c] = 0
        hm[c] += 1
        if len(hm) == 2:
            if i-left+1 > maxLen:
                maxLen = i-left+1
                res = s[left:i+1]
        while len(hm) > 2:
            c = s[left]
            if hm[c] > 0: hm[c] -= 1
            if hm[c] == 0: del hm[c]
            left += 1
    return res


print longestSub("abaccc")